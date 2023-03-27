from .decorators import public, initialise
from .orm import Storage

env = {
    "public": public,
    "initialise": initialise,
    "Storage": Storage
}