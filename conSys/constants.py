from enum import Enum


class APITerms(Enum):
    """
    Defines common endpoint terms used in the API
    """
    API = 'api'
    SYSTEMS = 'systems'
    FOIS = 'featuresOfInterest'
    DATASTREAMS = 'datastreams'
    OBSERVATIONS = 'observations'
    TASKING = 'controls'
    SAMPLING_FEATURES = 'samplingFeatures'
    PROCEDURES = 'procedures'
    DEPLOYMENTS = 'deployments'
    PROPERTIES = 'properties'


class SystemTypes(Enum):
    """
    Defines the system types
    """
    FEATURE = "Feature"


class ObservationFormat(Enum):
    """
    Defines common observation formats
    """
    JSON = "application/om+json"
    XML = "application/om+xml"
    SWE_XML = "application/swe+xml"
    SWE_JSON = "application/swe+json"
    SWE_CSV = "application/swe+csv"
    SWE_BINARY = "application/swe+binary"
