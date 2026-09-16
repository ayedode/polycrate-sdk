from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_kind_enum import ContentKindEnum, check_content_kind_enum
from ..models.conversation_kind_enum import ConversationKindEnum, check_conversation_kind_enum
from ..models.message_status_enum import MessageStatusEnum, check_message_status_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_simple import ConversationSimple
    from ..models.organization_simple import OrganizationSimple


T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """Full serializer for Message detail views and CRUD operations.
    Following S3 pattern with comprehensive fields and validation.

        Attributes:
            id (UUID):
            name (str):
            organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            conversation (ConversationSimple):
            meta (Any): Message metadata as JSON object
            config (Any): Message configuration as JSON object
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            kind (ConversationKindEnum | Unset): * `generic` - Generic
                * `zammad` - Zammad
                * `slack` - Slack
                * `discord` - Discord
                * `telegram` - Telegram
                * `msteams` - Microsoft Teams
                * `email` - Email
            status (MessageStatusEnum | Unset): * `pending` - Pending
                * `requested` - Requested
                * `delivered` - Delivered
                * `error` - Error
                * `deleted` - Deleted
            content (str | Unset): The actual message content
            content_kind (ContentKindEnum | Unset): * `text` - Text
                * `markdown` - Markdown
                * `html` - HTML
                * `json` - JSON
                * `yaml` - YAML
            provider_id (None | str | Unset):
    """

    id: UUID
    name: str
    organization: OrganizationSimple
    conversation: ConversationSimple
    meta: Any
    config: Any
    created_at: datetime.datetime
    updated_at: datetime.datetime
    kind: ConversationKindEnum | Unset = UNSET
    status: MessageStatusEnum | Unset = UNSET
    content: str | Unset = UNSET
    content_kind: ContentKindEnum | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        organization = self.organization.to_dict()

        conversation = self.conversation.to_dict()

        meta = self.meta

        config = self.config

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        content = self.content

        content_kind: str | Unset = UNSET
        if not isinstance(self.content_kind, Unset):
            content_kind = self.content_kind

        provider_id: None | str | Unset
        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = self.provider_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "organization": organization,
                "conversation": conversation,
                "meta": meta,
                "config": config,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if status is not UNSET:
            field_dict["status"] = status
        if content is not UNSET:
            field_dict["content"] = content
        if content_kind is not UNSET:
            field_dict["content_kind"] = content_kind
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_simple import ConversationSimple  # noqa: PLC0415
        from ..models.organization_simple import OrganizationSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        conversation = ConversationSimple.from_dict(d.pop("conversation"))

        meta = d.pop("meta")

        config = d.pop("config")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _kind = d.pop("kind", UNSET)
        kind: ConversationKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_conversation_kind_enum(_kind)

        _status = d.pop("status", UNSET)
        status: MessageStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_message_status_enum(_status)

        content = d.pop("content", UNSET)

        _content_kind = d.pop("content_kind", UNSET)
        content_kind: ContentKindEnum | Unset
        if isinstance(_content_kind, Unset):
            content_kind = UNSET
        else:
            content_kind = check_content_kind_enum(_content_kind)

        def _parse_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_id = _parse_provider_id(d.pop("provider_id", UNSET))

        message = cls(
            id=id,
            name=name,
            organization=organization,
            conversation=conversation,
            meta=meta,
            config=config,
            created_at=created_at,
            updated_at=updated_at,
            kind=kind,
            status=status,
            content=content,
            content_kind=content_kind,
            provider_id=provider_id,
        )

        message.additional_properties = d
        return message

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
