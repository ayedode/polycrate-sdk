from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.content_kind_enum import ContentKindEnum, check_content_kind_enum
from ..models.conversation_kind_enum import ConversationKindEnum, check_conversation_kind_enum
from ..models.message_status_enum import MessageStatusEnum, check_message_status_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessagePostRequest")


@_attrs_define
class MessagePostRequest:
    """Serializer for Message creation.
    Following S3 pattern with validation and create logic.

        Attributes:
            name (str):
            conversation (UUID): Conversation this message belongs to (required)
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
            organization (None | Unset | UUID): Organization that owns this message
            meta (Any | Unset): Message metadata as JSON object
            config (Any | Unset): Message configuration as JSON object
    """

    name: str
    conversation: UUID
    kind: ConversationKindEnum | Unset = UNSET
    status: MessageStatusEnum | Unset = UNSET
    content: str | Unset = UNSET
    content_kind: ContentKindEnum | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    organization: None | Unset | UUID = UNSET
    meta: Any | Unset = UNSET
    config: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        conversation = str(self.conversation)

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

        organization: None | str | Unset
        if isinstance(self.organization, Unset):
            organization = UNSET
        elif isinstance(self.organization, UUID):
            organization = str(self.organization)
        else:
            organization = self.organization

        meta = self.meta

        config = self.config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "conversation": conversation,
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
        if organization is not UNSET:
            field_dict["organization"] = organization
        if meta is not UNSET:
            field_dict["meta"] = meta
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("conversation", (None, str(self.conversation), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.status, Unset):
            files.append(("status", (None, str(self.status).encode(), "text/plain")))

        if not isinstance(self.content, Unset):
            files.append(("content", (None, str(self.content).encode(), "text/plain")))

        if not isinstance(self.content_kind, Unset):
            files.append(("content_kind", (None, str(self.content_kind).encode(), "text/plain")))

        if not isinstance(self.provider_id, Unset):
            if isinstance(self.provider_id, str):
                files.append(("provider_id", (None, str(self.provider_id).encode(), "text/plain")))
            else:
                files.append(("provider_id", (None, str(self.provider_id).encode(), "text/plain")))

        if not isinstance(self.organization, Unset):
            if isinstance(self.organization, UUID):
                files.append(("organization", (None, str(self.organization), "text/plain")))
            else:
                files.append(("organization", (None, str(self.organization).encode(), "text/plain")))

        if not isinstance(self.meta, Unset):
            files.append(("meta", (None, str(self.meta).encode(), "text/plain")))

        if not isinstance(self.config, Unset):
            files.append(("config", (None, str(self.config).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        conversation = UUID(d.pop("conversation"))

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

        def _parse_organization(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_type_0 = UUID(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization = _parse_organization(d.pop("organization", UNSET))

        meta = d.pop("meta", UNSET)

        config = d.pop("config", UNSET)

        message_post_request = cls(
            name=name,
            conversation=conversation,
            kind=kind,
            status=status,
            content=content,
            content_kind=content_kind,
            provider_id=provider_id,
            organization=organization,
            meta=meta,
            config=config,
        )

        message_post_request.additional_properties = d
        return message_post_request

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
