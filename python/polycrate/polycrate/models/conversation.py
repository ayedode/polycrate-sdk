from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conversation_kind_enum import ConversationKindEnum, check_conversation_kind_enum
from ..models.conversation_status_enum import ConversationStatusEnum, check_conversation_status_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_provider_simple import ConversationProviderSimple
    from ..models.message_list import MessageList
    from ..models.organization_simple import OrganizationSimple


T = TypeVar("T", bound="Conversation")


@_attrs_define
class Conversation:
    """Full serializer for Conversation detail views and CRUD operations.
    Following S3 pattern with comprehensive fields and validation.

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
            organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            conversation_provider (ConversationProviderSimple):
            messages (list[MessageList]):
            meta (Any): Conversation metadata as JSON object
            config (Any): Conversation configuration as JSON object
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            status (ConversationStatusEnum | Unset): * `closed` - Closed
                * `waiting_for_operator` - Waiting for Operator
                * `waiting_for_user` - Waiting for User
                * `deleted` - Deleted
            provider_id (None | str | Unset):
    """

    id: UUID
    name: str
    kind: ConversationKindEnum
    organization: OrganizationSimple
    conversation_provider: ConversationProviderSimple
    messages: list[MessageList]
    meta: Any
    config: Any
    created_at: datetime.datetime
    updated_at: datetime.datetime
    status: ConversationStatusEnum | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        kind: str = self.kind

        organization = self.organization.to_dict()

        conversation_provider = self.conversation_provider.to_dict()

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        meta = self.meta

        config = self.config

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

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
                "kind": kind,
                "organization": organization,
                "conversation_provider": conversation_provider,
                "messages": messages,
                "meta": meta,
                "config": config,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_provider_simple import ConversationProviderSimple  # noqa: PLC0415
        from ..models.message_list import MessageList  # noqa: PLC0415
        from ..models.organization_simple import OrganizationSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        kind = check_conversation_kind_enum(d.pop("kind"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        conversation_provider = ConversationProviderSimple.from_dict(d.pop("conversation_provider"))

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = MessageList.from_dict(messages_item_data)

            messages.append(messages_item)

        meta = d.pop("meta")

        config = d.pop("config")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        _status = d.pop("status", UNSET)
        status: ConversationStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_conversation_status_enum(_status)

        def _parse_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_id = _parse_provider_id(d.pop("provider_id", UNSET))

        conversation = cls(
            id=id,
            name=name,
            kind=kind,
            organization=organization,
            conversation_provider=conversation_provider,
            messages=messages,
            meta=meta,
            config=config,
            created_at=created_at,
            updated_at=updated_at,
            status=status,
            provider_id=provider_id,
        )

        conversation.additional_properties = d
        return conversation

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
