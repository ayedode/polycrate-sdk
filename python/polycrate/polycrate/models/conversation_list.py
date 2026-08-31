from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conversation_kind_enum import ConversationKindEnum, check_conversation_kind_enum
from ..models.conversation_status_enum import ConversationStatusEnum, check_conversation_status_enum

if TYPE_CHECKING:
    from ..models.conversation_provider_simple import ConversationProviderSimple
    from ..models.organization_simple import OrganizationSimple


T = TypeVar("T", bound="ConversationList")


@_attrs_define
class ConversationList:
    """Lightweight serializer for Conversation list views.
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
            status (ConversationStatusEnum): * `closed` - Closed
                * `waiting_for_operator` - Waiting for Operator
                * `waiting_for_user` - Waiting for User
                * `deleted` - Deleted
            organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            conversation_provider (ConversationProviderSimple):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            provider_id (None | str):
    """

    id: UUID
    name: str
    kind: ConversationKindEnum
    status: ConversationStatusEnum
    organization: OrganizationSimple
    conversation_provider: ConversationProviderSimple
    created_at: datetime.datetime
    updated_at: datetime.datetime
    provider_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        kind: str = self.kind

        status: str = self.status

        organization = self.organization.to_dict()

        conversation_provider = self.conversation_provider.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        provider_id: None | str
        provider_id = self.provider_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "kind": kind,
                "status": status,
                "organization": organization,
                "conversation_provider": conversation_provider,
                "created_at": created_at,
                "updated_at": updated_at,
                "provider_id": provider_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_provider_simple import ConversationProviderSimple
        from ..models.organization_simple import OrganizationSimple

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        kind = check_conversation_kind_enum(d.pop("kind"))

        status = check_conversation_status_enum(d.pop("status"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        conversation_provider = ConversationProviderSimple.from_dict(d.pop("conversation_provider"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_provider_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_id = _parse_provider_id(d.pop("provider_id"))

        conversation_list = cls(
            id=id,
            name=name,
            kind=kind,
            status=status,
            organization=organization,
            conversation_provider=conversation_provider,
            created_at=created_at,
            updated_at=updated_at,
            provider_id=provider_id,
        )

        conversation_list.additional_properties = d
        return conversation_list

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
