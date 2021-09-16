import logging
import os
import pandas as pd

def load_aws_dataset(filename: str, compression: str = 'zip') -> pd.DataFrame:
	"""
		Loads the AWS pricing dataset from the data folders.
		Already sets the correct data type for datetime values,
		set the index column, and load from zipped file.

		Return:
		- dataframe with the pricing data
	"""

	if not os.path.exists(filename):
	    raise IOError(f'File "{filename}" not found error!')

	return pd.read_csv(filename, 
	                   parse_dates=['Timestamp'],
	                   compression=compression, 
	                   index_col=0)

def remove_consecutive_repeated_price_entries(in_ser: pd.Series) -> pd.Series:
    """
     This function removes the repeated price entries in the Series. If
     we want to calculate the price update interval, but if it doesn't
     change, we need to get to the next one that actually has a change.

     Note that we do not remove only repeated values with .drop_duplicates()
     as this will remove non-consecutive values. This will lead to a wrong
     price list when there is a price change with ups and downs with repeated
     values.

     Input:
     - in_ser: Pandas Series with the price list
     
     Output:
     - out_ser: Pandas Series without the consecutive repeated prices.
    """
    if not isinstance(in_ser, pd.Series):
        raise TypeError('Wrong parameter passed. Excepted a Pandas Series.')
    
    aux = in_ser.dropna()
    return aux.loc[aux.shift() != aux]

def calc_pdf_price_update_interval_seconds(in_df: pd.DataFrame) -> pd.Series:
    """
        This method calculates the probabilistic density function of the
        price update timings.
        
        Input:
        - a pd.DataFrame of Timestamp in the format "%Y-%m-%d %H:%M:%S"
        
        Output:
        - pd.DataFrame with the curve description
    """
    idx_ser = in_df.reset_index().loc[:, 'Timestamp']
    delta_ser = idx_ser - idx_ser.shift()
    return delta_ser.dropna().dt.total_seconds()\
                    .describe()\
                    .rename(in_df.name)\
                    .to_frame()

def generate_price_update_interval(in_df: pd.DataFrame) -> pd.DataFrame:
    """
        This function generates the pdf for the price update interval.
        Input:
        - pd.DataFrame with all instances and their prices
        Output:
        - pd.DataFrame with the distribution parameters.
    """

    uplist = [(cdf.pipe(remove_consecutive_repeated_price_entries)\
                  .pipe(calc_pdf_price_update_interval_seconds))\
                  for _, cdf in in_df.items()]
    
    return pd.concat(uplist, axis=1).iloc[1:].dropna(axis=1, how='all')
