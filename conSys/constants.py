from enum import Enum


class APITerms(Enum):
    """
    Defines common endpoint terms used in the API
    """
    API = 'api'
    COLLECTIONS = 'collections'
    COMMANDS = 'commands'
    COMPONENTS = 'components'
    CONFORMANCE = 'conformance'
    CONTROL_STREAMS = 'controls'
    DATASTREAMS = 'datastreams'
    DEPLOYMENTS = 'deployments'
    FOIS = 'featuresOfInterest'
    ITEMS = 'items'
    OBSERVATIONS = 'observations'
    PROCEDURES = 'procedures'
    PROPERTIES = 'properties'
    SAMPLING_FEATURES = 'samplingFeatures'
    SCHEMA = 'schema'
    STATUS = 'status'
    SYSTEMS = 'systems'
    TASKING = 'controls'
    UNDEFINED = ''


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
