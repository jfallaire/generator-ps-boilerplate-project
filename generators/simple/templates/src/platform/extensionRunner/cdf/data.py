"""
    - THIS FILE IS GENERATED -

dependencies/CMF.Net/Cmf/Data/CoveoData.jid

"""

from attr import attrib, attrs
from datetime import datetime
from enum import auto
from typing import Any, List, Optional as Opt
from .root import CASING, CoveoInterface, ExceptionBase, JidEnumFlag, JidType


class ExprOp(JidEnumFlag):
    Add: int = auto()
    Sub: int = auto()
    Mul: int = auto()
    Div: int = auto()
    Mod: int = auto()
    Power: int = auto()
    ShiftL: int = auto()
    ShiftR: int = auto()
    Neg: int = auto()
    Eq: int = auto()
    Ne: int = auto()
    Lt: int = auto()
    Le: int = auto()
    Gt: int = auto()
    Ge: int = auto()
    Not: int = auto()
    AndAlso: int = auto()
    OrElse: int = auto()
    BitAnd: int = auto()
    BitOr: int = auto()
    BitNot: int = auto()
    BitXor: int = auto()
    Contains: int = auto()
    Field: int = auto()
    Cte: int = auto()
    Alias: int = auto()
    New: int = auto()
    Select: int = auto()
    SelectMany: int = auto()
    Table: int = auto()
    Join: int = auto()
    Where: int = auto()
    OrderByA: int = auto()
    OrderByD: int = auto()
    ThenByA: int = auto()
    ThenByD: int = auto()
    Min: int = auto()
    Max: int = auto()
    Sum: int = auto()
    Avg: int = auto()
    Count: int = auto()
    Skip: int = auto()
    Take: int = auto()
    Union: int = auto()
    Intersect: int = auto()
    Diff: int = auto()
    Distinct: int = auto()
    GroupBy: int = auto()
    GroupJoin: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class Expr(JidType, hint="Coveo.Data.Expr"):
    op: Opt[ExprOp] = None

    def __init__(self, *, op: Opt[ExprOp] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExprAlias(Expr, hint="Coveo.Data.ExprAlias"):
    number: Opt[int] = None

    def __init__(self, *, number: Opt[int] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExprTable(Expr, hint="Coveo.Data.ExprTable"):
    name: Opt[str] = None
    alias: Opt[ExprAlias] = None

    def __init__(self, *, name: Opt[str] = None, alias: Opt[ExprAlias] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExprJoin(Expr, hint="Coveo.Data.ExprJoin"):
    outer: Opt[Expr] = None
    inner: Opt[Expr] = None
    outer_key_selector: Opt[Expr] = None
    inner_key_selector: Opt[Expr] = None

    def __init__(
        self,
        *,
        outer: Opt[Expr] = None,
        inner: Opt[Expr] = None,
        outer_key_selector: Opt[Expr] = None,
        inner_key_selector: Opt[Expr] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExprSelect(Expr, hint="Coveo.Data.ExprSelect"):
    source: Opt[Expr] = None
    selector: Opt[Expr] = None

    def __init__(self, *, source: Opt[Expr] = None, selector: Opt[Expr] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExprWhere(Expr, hint="Coveo.Data.ExprWhere"):
    source: Opt[Expr] = None
    filter_: Opt[Expr] = attrib(default=None, metadata={CASING: "Filter"})

    def __init__(
        self, *, source: Opt[Expr] = None, filter_: Opt[Expr] = attrib(default=None, metadata={CASING: "Filter"})
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExprBinary(Expr, hint="Coveo.Data.ExprBinary"):
    left: Opt[Expr] = None
    right: Opt[Expr] = None

    def __init__(self, *, left: Opt[Expr] = None, right: Opt[Expr] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExprUnary(Expr, hint="Coveo.Data.ExprUnary"):
    expr: Opt[Expr] = None

    def __init__(self, *, expr: Opt[Expr] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExprField(Expr, hint="Coveo.Data.ExprField"):
    expr: Opt[Expr] = None
    name: Opt[str] = None

    def __init__(self, *, expr: Opt[Expr] = None, name: Opt[str] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExprCte(Expr, hint="Coveo.Data.ExprCte"):
    value: Opt[Any] = None

    def __init__(self, *, value: Opt[Any] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExprNew(Expr, hint="Coveo.Data.ExprNew"):
    exprs: Opt[List[Expr]] = None

    def __init__(self, *, exprs: Opt[List[Expr]] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExprContains(Expr, hint="Coveo.Data.ExprContains"):
    left: Opt[Expr] = None
    right: Opt[Expr] = None

    def __init__(self, *, left: Opt[Expr] = None, right: Opt[Expr] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExprSelectMany(Expr, hint="Coveo.Data.ExprSelectMany"):
    source1: Opt[Expr] = None
    source2: Opt[Expr] = None
    alias2: Opt[ExprAlias] = None

    def __init__(self, *, source1: Opt[Expr] = None, source2: Opt[Expr] = None, alias2: Opt[ExprAlias] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExprOrderBy(Expr, hint="Coveo.Data.ExprOrderBy"):
    source: Opt[Expr] = None
    key: Opt[Expr] = None

    def __init__(self, *, source: Opt[Expr] = None, key: Opt[Expr] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class ExprSkipOrTake(Expr, hint="Coveo.Data.ExprSkipOrTake"):
    source: Opt[Expr] = None
    how_many: Opt[int] = None

    def __init__(self, *, source: Opt[Expr] = None, how_many: Opt[int] = None) -> None:
        ...


class DbRowState(JidEnumFlag):
    Added: int = auto()
    Updated: int = auto()
    Deleted: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class DbRow(JidType, hint="Coveo.Data.DbRow"):
    row_id: Opt[int] = None
    row_state: Opt[DbRowState] = None
    delta_id: Opt[int] = None
    old_delta_id: Opt[int] = None

    def __init__(
        self,
        *,
        row_id: Opt[int] = None,
        row_state: Opt[DbRowState] = None,
        delta_id: Opt[int] = None,
        old_delta_id: Opt[int] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class DbLink(DbRow, hint="Coveo.Data.DbLink"):
    from_row_id: Opt[int] = None
    to_row_id: Opt[int] = None

    def __init__(self, *, from_row_id: Opt[int] = None, to_row_id: Opt[int] = None) -> None:
        ...


class DbErrorKind(JidEnumFlag):
    Appl: int = auto()
    Unexpected: int = auto()
    ConcurrentUpdate: int = auto()
    Duplicate: int = auto()
    BadFk: int = auto()
    MissingValue: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class DbError(JidType, hint="Coveo.Data.DbError"):
    row_id: Opt[str] = None
    kind: Opt[DbErrorKind] = None
    msg: Opt[str] = None

    def __init__(self, *, row_id: Opt[str] = None, kind: Opt[DbErrorKind] = None, msg: Opt[str] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class DbErrorField(DbError, hint="Coveo.Data.DbErrorField"):
    field_name: Opt[str] = None
    field_value: Opt[Any] = None

    def __init__(self, *, field_name: Opt[str] = None, field_value: Opt[Any] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class OldToNewRowId(JidType, hint="Coveo.Data.OldToNewRowId"):
    old_id: Opt[int] = None
    new_id: Opt[int] = None

    def __init__(self, *, old_id: Opt[int] = None, new_id: Opt[int] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class DbDelta(JidType, hint="Coveo.Data.DbDelta"):
    what: Opt[List[DbRow]] = None
    who: Opt[str] = None
    when: Opt[datetime] = None
    why: Opt[str] = None
    delta_id: Opt[int] = None
    errors: Opt[List[DbError]] = None
    row_id_map: Opt[List[OldToNewRowId]] = None

    def __init__(
        self,
        *,
        what: Opt[List[DbRow]] = None,
        who: Opt[str] = None,
        when: Opt[datetime] = None,
        why: Opt[str] = None,
        delta_id: Opt[int] = None,
        errors: Opt[List[DbError]] = None,
        row_id_map: Opt[List[OldToNewRowId]] = None,
    ) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class DataException(ExceptionBase, hint="Coveo.Data.DataException"):
    def __init__(self) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class CommitException(DataException, hint="Coveo.Data.CommitException"):
    errors: Opt[List[DbError]] = None

    def __init__(self, *, errors: Opt[List[DbError]] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class DataTupleField(JidType, hint="Coveo.Data.DataTupleField"):
    name: Opt[str] = None
    value: Opt[Any] = None

    def __init__(self, *, name: Opt[str] = None, value: Opt[Any] = None) -> None:
        ...


@attrs(kw_only=True, auto_attribs=True)
class DataTuple(JidType, hint="Coveo.Data.DataTuple"):
    tuple_id: Opt[str] = None
    tuple_type: Opt[str] = None
    tuple_fields: Opt[List[DataTupleField]] = None

    def __init__(
        self, *, tuple_id: Opt[str] = None, tuple_type: Opt[str] = None, tuple_fields: Opt[List[DataTupleField]] = None
    ) -> None:
        ...


class IDbServer(CoveoInterface):
    ...
