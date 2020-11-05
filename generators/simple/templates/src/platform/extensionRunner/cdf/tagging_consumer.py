"""
    - THIS FILE IS GENERATED -

CoveoInterfaces/CoveoInterfaces/CoveoTaggingConsumer.jid

"""

from attr import attrib, attrs
from enum import auto
from typing import List, Optional as Opt
from .root import CASING, CoveoInterface, JidEnumFlag, JidType, api
from .search_service import NameValuePair, QueryParamsForTagging
from .security_provider import SID


class OpCode(JidEnumFlag):
    """List of the codes for tagging operations

    Attributes:
        InvalidTagOpCode: Invalid tag operation.
        Tag: Add a tag on a given set of documents.
        UnTag: Remove a tag on a given set of documents.
        ClearTag: Remove the given tag name-value pairs from all documents in the index.
        ClearAllTagValues: Clear the given tags from all documents in the index.
        ClearDocumentTags: Clear the given tags from the targeted document.
        ClearDocumentsTags: Clear the given tags from the documents targeted by a query.
    """

    InvalidTagOpCode: int = auto()
    Tag: int = auto()
    UnTag: int = auto()
    ClearTag: int = auto()
    ClearAllTagValues: int = auto()
    ClearDocumentTags: int = auto()
    ClearDocumentsTags: int = auto()


@attrs(kw_only=True, auto_attribs=True)
class TaggingCommand(JidType, hint="Coveo.TaggingCommand"):
    """The definition of tagging command.

    Attributes:
        op_code: Whether to tag, untag, or clear the tag.
        query_params: Info about the query for perform tagging by query.
        target_document: Document (to tag/untag). (Used by single-document tagging, not used by tagging by query.)
        name_value_pairs: List of tag field name, tag value name for batch tagging (needed for tagging by query).
        robot: Whether tagging is performed by a robot. We commit less often for robots.
        super_user_mode: Whether tagging is performed in super user mode.
        sid: The SIDDeclarator for the user performing the tagging request, will be used to construct the query info in all mirrors.
        sid_for_internal_sid: Will be used to construct the query info in all mirrors.
        full_user_name: Full user name. Set only when tagging with document keys (when m_QueryInfo in null).
    """

    op_code: Opt[OpCode] = None
    query_params: Opt[QueryParamsForTagging] = None
    target_document: Opt[str] = None
    name_value_pairs: Opt[List[NameValuePair]] = None
    robot: Opt[bool] = None
    super_user_mode: Opt[bool] = None
    sid: Opt[SID] = attrib(default=None, metadata={CASING: "SID"})
    sid_for_internal_sid: Opt[List[SID]] = attrib(default=None, metadata={CASING: "SIDForInternalSID"})
    full_user_name: Opt[str] = None

    def __init__(
        self,
        *,
        op_code: Opt[OpCode] = None,
        query_params: Opt[QueryParamsForTagging] = None,
        target_document: Opt[str] = None,
        name_value_pairs: Opt[List[NameValuePair]] = None,
        robot: Opt[bool] = None,
        super_user_mode: Opt[bool] = None,
        sid: Opt[SID] = attrib(default=None, metadata={CASING: "SID"}),
        sid_for_internal_sid: Opt[List[SID]] = attrib(default=None, metadata={CASING: "SIDForInternalSID"}),
        full_user_name: Opt[str] = None,
    ) -> None:
        """

        Parameters:
            op_code: Whether to tag, untag, or clear the tag.
            query_params: Info about the query for perform tagging by query.
            target_document: Document (to tag/untag). (Used by single-document tagging, not used by tagging by query.)
            name_value_pairs: List of tag field name, tag value name for batch tagging (needed for tagging by query).
            robot: Whether tagging is performed by a robot. We commit less often for robots.
            super_user_mode: Whether tagging is performed in super user mode.
            sid: The SIDDeclarator for the user performing the tagging request, will be used to construct the query info in all mirrors.
            sid_for_internal_sid: Will be used to construct the query info in all mirrors.
            full_user_name: Full user name. Set only when tagging with document keys (when m_QueryInfo in null).
        """


class ITaggingConsumer(CoveoInterface):
    @api("POST/tag")
    def update_tagging(self, *, tagging_command: TaggingCommand) -> None:
        ...
