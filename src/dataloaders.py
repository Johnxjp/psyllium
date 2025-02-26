import pandas as pd

from utils import convert_drainage_values
from schemas import (
    CHORIZON_COLUMN_NAMES,
    AREA_LEGEND_COLUMN_NAMES,
    MAPUNIT_COLUMN_NAMES,
    COMPONENT_COLUMN_NAMES,
)


def load_chorizon_db(abs_filename: str) -> pd.DataFrame:
    """
    Loads the chorizon.txt file in each area directoryand converts drainage values to inches per hour
    Also fills in missing values for attributes with the regular values.

    Returns a dataframe with the chorizon data.
    """
    df = pd.read_csv(abs_filename, delimiter="|", names=CHORIZON_COLUMN_NAMES)
    df["ksat_l"] = df["ksat_l"].apply(convert_drainage_values)
    df["ksat_r"] = df["ksat_r"].apply(convert_drainage_values)
    df["ksat_h"] = df["ksat_h"].apply(convert_drainage_values)
    attribute_cols = (
        ["sandtotal_l", "sandtotal_r", "sandtotal_h"],
        ["silttotal_l", "silttotal_r", "silttotal_h"],
        ["claytotal_l", "claytotal_r", "claytotal_h"],
        ["ph1to1h2o_l", "ph1to1h2o_l", "ph1to1h2o_l"],
        ["ksat_l", "ksat_r", "ksat_h"],
    )
    for l, r, h in attribute_cols:
        df[l] = df[l].where(~df[l].isna(), df[r])
        df[h] = df[h].where(~df[h].isna(), df[r])

    return df


def load_area_legend_db(abs_filename: str) -> pd.DataFrame:
    """
    Loads the legend.txt file in each area directory

    Returns a dataframe with the area legend data.
    """
    return pd.read_csv(abs_filename, delimiter="|", names=AREA_LEGEND_COLUMN_NAMES)


def load_mapunit_db(abs_filename: str) -> pd.DataFrame:
    """
    Loads the mapunit.txt file in each area directory

    Returns a dataframe with the mapunit data.
    """
    return pd.read_csv(abs_filename, delimiter="|", names=MAPUNIT_COLUMN_NAMES)


def load_component_db(abs_filename: str) -> pd.DataFrame:
    """
    Loads the component.txt file in each area directory
    """
    return pd.read_csv(abs_filename, delimiter="|", names=COMPONENT_COLUMN_NAMES)
