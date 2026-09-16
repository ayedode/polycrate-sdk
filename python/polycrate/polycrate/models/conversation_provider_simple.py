from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conversation_kind_enum import ConversationKindEnum, check_conversation_kind_enum

if TYPE_CHECKING:
    from ..models.organization_simple import OrganizationSimple


T = TypeVar("T", bound="ConversationProviderSimple")


@_attrs_define
class ConversationProviderSimple:
    """
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
        provider_id (None | str):
    """

    id: UUID
    name: str
    kind: ConversationKindEnum
    organization: OrganizationSimple
    provider_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        kind: str = self.kind

        organization = self.organization.to_dict()

        provider_id: None | str
        provider_id = self.provider_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "kind": kind,
                "organization": organization,
                "provider_id": provider_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_simple import OrganizationSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        kind = check_conversation_kind_enum(d.pop("kind"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        def _parse_provider_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        provider_id = _parse_provider_id(d.pop("provider_id"))

        conversation_provider_simple = cls(
            id=id,
            name=name,
            kind=kind,
            organization=organization,
            provider_id=provider_id,
        )

        conversation_provider_simple.additional_properties = d
        return conversation_provider_simple

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
