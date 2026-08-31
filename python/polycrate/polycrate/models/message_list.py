from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_kind_enum import ContentKindEnum, check_content_kind_enum
from ..models.conversation_kind_enum import ConversationKindEnum, check_conversation_kind_enum
from ..models.message_status_enum import MessageStatusEnum, check_message_status_enum

if TYPE_CHECKING:
    from ..models.conversation_simple import ConversationSimple
    from ..models.organization_simple import OrganizationSimple


T = TypeVar("T", bound="MessageList")


@_attrs_define
class MessageList:
    """Lightweight serializer for Message list views.
    Following S3 pattern with simple nested serializers.

        Attributes:
            id (UUID):
            name (str):
            kind (ConversationKindEnum): * `generic` - Generic
                * `zammad` - Zammad
                * `slack` - Slack
                * `discord` - Discord
                * `telegram` - Telegram
                * `msteams` - Microsoft Teams
                * `email` - Email
            status (MessageStatusEnum): * `pending` - Pending
                * `requested` - Requested
                * `delivered` - Delivered
                * `error` - Error
                * `deleted` - Deleted
            content (str): The actual message content
            content_kind (ContentKindEnum): * `text` - Text
                * `markdown` - Markdown
                * `html` - HTML
                * `json` - JSON
                * `yaml` - YAML
            organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            conversation (ConversationSimple):
            meta (Any): Message metadata and additional information
            config (Any): Message-specific configuration settings
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
    """

    id: UUID
    name: str
    kind: ConversationKindEnum
    status: MessageStatusEnum
    content: str
    content_kind: ContentKindEnum
    organization: OrganizationSimple
    conversation: ConversationSimple
    meta: Any
    config: Any
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        kind: str = self.kind

        status: str = self.status

        content = self.content

        content_kind: str = self.content_kind

        organization = self.organization.to_dict()

        conversation = self.conversation.to_dict()

        meta = self.meta

        config = self.config

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "kind": kind,
                "status": status,
                "content": content,
                "content_kind": content_kind,
                "organization": organization,
                "conversation": conversation,
                "meta": meta,
                "config": config,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_simple import ConversationSimple
        from ..models.organization_simple import OrganizationSimple

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        kind = check_conversation_kind_enum(d.pop("kind"))

        status = check_message_status_enum(d.pop("status"))

        content = d.pop("content")

        content_kind = check_content_kind_enum(d.pop("content_kind"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        conversation = ConversationSimple.from_dict(d.pop("conversation"))

        meta = d.pop("meta")

        config = d.pop("config")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        message_list = cls(
            id=id,
            name=name,
            kind=kind,
            status=status,
            content=content,
            content_kind=content_kind,
            organization=organization,
            conversation=conversation,
            meta=meta,
            config=config,
            created_at=created_at,
            updated_at=updated_at,
        )

        message_list.additional_properties = d
        return message_list

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
