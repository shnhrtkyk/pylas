import numpy as np


def point_format_to_dtype(point_format):
    return [dimensions[dim_name] for dim_name in point_format]


def bit_transform(x, low, high):
    return np.right_shift(np.bitwise_and(x, 2 ** high - 1), low)


RETURN_NUMBER_LOW_BIT = 0
RETURN_NUMBER_HIGH_BIT = 3
NUMBER_OF_RETURNS_LOW_BIT = 3
NUMBER_OF_RETURNS_HIGH_BIT = 6
SCAN_DIRECTION_FLAG_LOW_BIT = 6
SCAN_DIRECTION_FLAG_HIGH_BIT = 7
EDGE_OF_FLIGHT_LINE_LOW_BIT = 7
EDGE_OF_FLIGHT_LINE_HIGH_BIT = 8

dimensions = {
    'X': ('X', 'u4'),
    'Y': ('Y', 'u4'),
    'Z': ('Z', 'u4'),
    'intensity': ('intensity', 'u2'),
    'bit_fields': ('bit_fields', 'u1'),
    'classification': ('classification', 'u1'),
    'scan_angle_rank': ('scan_angle_rank', 'i1'),
    'user_data': ('user_data', 'u1'),
    'point_source_id': ('point_source_id', 'u2'),
    'gps_time': ('gps_time', 'f8'),
    'red': ('red', 'u2'),
    'green': ('green', 'u2'),
    'blue': ('blue', 'u2'),
}

point_format_0 = (
    'X',
    'Y',
    'Z',
    'intensity',
    'bit_fields',
    'classification',
    'scan_angle_rank',
    'user_data',
    'point_source_id'
)

point_formats = (
    point_format_0,
    point_format_0 + ('gps_time',),
    point_format_0 + ('red', 'green', 'blue',),
    point_format_0 + ('red', 'green', 'blue', 'gps_time',),
)

point_formats_dtype = tuple(np.dtype(point_format_to_dtype(point_fmt)) for point_fmt in point_formats)
