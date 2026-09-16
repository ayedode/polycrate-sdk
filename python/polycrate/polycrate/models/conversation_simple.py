from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conversation_kind_enum import ConversationKindEnum, check_conversation_kind_enum
from ..models.conversation_status_enum import ConversationStatusEnum, check_conversation_status_enum

if TYPE_CHECKING:
    from ..models.organization_simple import OrganizationSimple


T = TypeVar("T", bound="ConversationSimple")


@_attrs_define
class ConversationSimple:
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
        status (ConversationStatusEnum): * `closed` - Closed
            * `waiting_for_operator` - Waiting for Operator
            * `waiting_for_user` - Waiting for User
            * `deleted` - Deleted
        organization (OrganizationSimple): Simple Organization serializer for nested representations.

            Includes `url` field for direct navigation.
    """

    id: UUID
    name: str
    kind: ConversationKindEnum
    status: ConversationStatusEnum
    organization: OrganizationSimple
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        kind: str = self.kind

        status: str = self.status

        organization = self.organization.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "kind": kind,
                "status": status,
                "organization": organization,
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

        status = check_conversation_status_enum(d.pop("status"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        conversation_simple = cls(
            id=id,
            name=name,
            kind=kind,
            status=status,
            organization=organization,
        )

        conversation_simple.additional_properties = d
        return conversation_simple

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
