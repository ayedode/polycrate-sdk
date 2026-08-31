from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_kind_enum import ContentKindEnum, check_content_kind_enum
from ..models.message_status_enum import MessageStatusEnum, check_message_status_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageUpdate")


@_attrs_define
class MessageUpdate:
    """Serializer for Message updates.
    Following S3 pattern with restricted update fields.

        Attributes:
            id (UUID):
            name (str):
            organization (None | UUID): Organization that owns this message
            conversation (None | UUID): Conversation that this message belongs to
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
            meta (Any | Unset): Message metadata as JSON object
            config (Any | Unset): Message configuration as JSON object
    """

    id: UUID
    name: str
    organization: None | UUID
    conversation: None | UUID
    status: MessageStatusEnum | Unset = UNSET
    content: str | Unset = UNSET
    content_kind: ContentKindEnum | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    meta: Any | Unset = UNSET
    config: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        organization: None | str
        if isinstance(self.organization, UUID):
            organization = str(self.organization)
        else:
            organization = self.organization

        conversation: None | str
        if isinstance(self.conversation, UUID):
            conversation = str(self.conversation)
        else:
            conversation = self.conversation

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

        meta = self.meta

        config = self.config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "organization": organization,
                "conversation": conversation,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if content is not UNSET:
            field_dict["content"] = content
        if content_kind is not UNSET:
            field_dict["content_kind"] = content_kind
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if meta is not UNSET:
            field_dict["meta"] = meta
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_organization(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_type_0 = UUID(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_conversation(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conversation_type_0 = UUID(data)

                return conversation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        conversation = _parse_conversation(d.pop("conversation"))

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

        meta = d.pop("meta", UNSET)

        config = d.pop("config", UNSET)

        message_update = cls(
            id=id,
            name=name,
            organization=organization,
            conversation=conversation,
            status=status,
            content=content,
            content_kind=content_kind,
            provider_id=provider_id,
            meta=meta,
            config=config,
        )

        message_update.additional_properties = d
        return message_update

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
