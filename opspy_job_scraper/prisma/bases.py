# -*- coding: utf-8 -*-
# code generated by Prisma. DO NOT EDIT.
# pyright: reportUnusedImport=false
# fmt: off

# global imports for type checking
from builtins import bool as _bool
from builtins import int as _int
from builtins import float as _float
from builtins import str as _str
import sys
import decimal
import datetime
from typing import (
    TYPE_CHECKING,
    Optional,
    Iterable,
    Iterator,
    Sequence,
    Callable,
    ClassVar,
    NoReturn,
    TypeVar,
    Generic,
    Mapping,
    Tuple,
    Union,
    List,
    Dict,
    Type,
    Any,
    Set,
    overload,
    cast,
)
from typing_extensions import TypedDict, Literal


LiteralString = str
# -- template models.py.jinja --
from pydantic import BaseModel

from . import fields, actions
from ._types import FuncType
from ._builder import serialize_base64
from ._compat import PYDANTIC_V2, ConfigDict

if TYPE_CHECKING:
    from .client import Prisma


_PrismaModelT = TypeVar('_PrismaModelT', bound='_PrismaModel')


class _PrismaModel(BaseModel):
    if PYDANTIC_V2:
        model_config: ClassVar[ConfigDict] = ConfigDict(
            use_enum_values=True,
            arbitrary_types_allowed=True,
            populate_by_name=True,
        )
    elif not TYPE_CHECKING:
        from ._compat import BaseConfig

        class Config(BaseConfig):
            use_enum_values: bool = True
            arbitrary_types_allowed: bool = True
            allow_population_by_field_name: bool = True
            json_encoders: Dict[Any, FuncType] = {
                fields.Base64: serialize_base64,
            }

    # TODO: ensure this is required by subclasses
    __prisma_model__: ClassVar[str]


class BaseCompany(_PrismaModel):
    __prisma_model__: ClassVar[Literal['Company']] = 'Company'  # pyright: ignore[reportIncompatibleVariableOverride]

    @classmethod
    def prisma(cls: Type[_PrismaModelT], client: Optional['Prisma'] = None) -> 'actions.CompanyActions[_PrismaModelT]':
        from .client import get_client

        return actions.CompanyActions[_PrismaModelT](client or get_client(), cls)


class BaseJobApplication(_PrismaModel):
    __prisma_model__: ClassVar[Literal['JobApplication']] = 'JobApplication'  # pyright: ignore[reportIncompatibleVariableOverride]

    @classmethod
    def prisma(cls: Type[_PrismaModelT], client: Optional['Prisma'] = None) -> 'actions.JobApplicationActions[_PrismaModelT]':
        from .client import get_client

        return actions.JobApplicationActions[_PrismaModelT](client or get_client(), cls)


class BaseJobPost(_PrismaModel):
    __prisma_model__: ClassVar[Literal['JobPost']] = 'JobPost'  # pyright: ignore[reportIncompatibleVariableOverride]

    @classmethod
    def prisma(cls: Type[_PrismaModelT], client: Optional['Prisma'] = None) -> 'actions.JobPostActions[_PrismaModelT]':
        from .client import get_client

        return actions.JobPostActions[_PrismaModelT](client or get_client(), cls)


class BaseJobTracker(_PrismaModel):
    __prisma_model__: ClassVar[Literal['JobTracker']] = 'JobTracker'  # pyright: ignore[reportIncompatibleVariableOverride]

    @classmethod
    def prisma(cls: Type[_PrismaModelT], client: Optional['Prisma'] = None) -> 'actions.JobTrackerActions[_PrismaModelT]':
        from .client import get_client

        return actions.JobTrackerActions[_PrismaModelT](client or get_client(), cls)


class BaseTag(_PrismaModel):
    __prisma_model__: ClassVar[Literal['Tag']] = 'Tag'  # pyright: ignore[reportIncompatibleVariableOverride]

    @classmethod
    def prisma(cls: Type[_PrismaModelT], client: Optional['Prisma'] = None) -> 'actions.TagActions[_PrismaModelT]':
        from .client import get_client

        return actions.TagActions[_PrismaModelT](client or get_client(), cls)


class BaseUploadedCv(_PrismaModel):
    __prisma_model__: ClassVar[Literal['UploadedCv']] = 'UploadedCv'  # pyright: ignore[reportIncompatibleVariableOverride]

    @classmethod
    def prisma(cls: Type[_PrismaModelT], client: Optional['Prisma'] = None) -> 'actions.UploadedCvActions[_PrismaModelT]':
        from .client import get_client

        return actions.UploadedCvActions[_PrismaModelT](client or get_client(), cls)


class BaseUser(_PrismaModel):
    __prisma_model__: ClassVar[Literal['User']] = 'User'  # pyright: ignore[reportIncompatibleVariableOverride]

    @classmethod
    def prisma(cls: Type[_PrismaModelT], client: Optional['Prisma'] = None) -> 'actions.UserActions[_PrismaModelT]':
        from .client import get_client

        return actions.UserActions[_PrismaModelT](client or get_client(), cls)


class BaseWorkExperience(_PrismaModel):
    __prisma_model__: ClassVar[Literal['WorkExperience']] = 'WorkExperience'  # pyright: ignore[reportIncompatibleVariableOverride]

    @classmethod
    def prisma(cls: Type[_PrismaModelT], client: Optional['Prisma'] = None) -> 'actions.WorkExperienceActions[_PrismaModelT]':
        from .client import get_client

        return actions.WorkExperienceActions[_PrismaModelT](client or get_client(), cls)


class BaseAccount(_PrismaModel):
    __prisma_model__: ClassVar[Literal['Account']] = 'Account'  # pyright: ignore[reportIncompatibleVariableOverride]

    @classmethod
    def prisma(cls: Type[_PrismaModelT], client: Optional['Prisma'] = None) -> 'actions.AccountActions[_PrismaModelT]':
        from .client import get_client

        return actions.AccountActions[_PrismaModelT](client or get_client(), cls)


class BaseSession(_PrismaModel):
    __prisma_model__: ClassVar[Literal['Session']] = 'Session'  # pyright: ignore[reportIncompatibleVariableOverride]

    @classmethod
    def prisma(cls: Type[_PrismaModelT], client: Optional['Prisma'] = None) -> 'actions.SessionActions[_PrismaModelT]':
        from .client import get_client

        return actions.SessionActions[_PrismaModelT](client or get_client(), cls)


class BaseVerificationToken(_PrismaModel):
    __prisma_model__: ClassVar[Literal['VerificationToken']] = 'VerificationToken'  # pyright: ignore[reportIncompatibleVariableOverride]

    @classmethod
    def prisma(cls: Type[_PrismaModelT], client: Optional['Prisma'] = None) -> 'actions.VerificationTokenActions[_PrismaModelT]':
        from .client import get_client

        return actions.VerificationTokenActions[_PrismaModelT](client or get_client(), cls)


