from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conversation_kind_enum import ConversationKindEnum, check_conversation_kind_enum

if TYPE_CHECKING:
    from ..models.credential_simple import CredentialSimple
    from ..models.organization_simple import OrganizationSimple


T = TypeVar("T", bound="ConversationProviderList")


@_attrs_define
class ConversationProviderList:
    """Lightweight serializer for ConversationProvider list views.
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
            organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            credential (CredentialSimple): Simple serializer for embedding Credential in other serializers.
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
    """

    id: UUID
    name: str
    kind: ConversationKindEnum
    organization: OrganizationSimple
    credential: CredentialSimple
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        kind: str = self.kind

        organization = self.organization.to_dict()

        credential = self.credential.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "kind": kind,
                "organization": organization,
                "credential": credential,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_simple import CredentialSimple  # noqa: PLC0415
        from ..models.organization_simple import OrganizationSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        kind = check_conversation_kind_enum(d.pop("kind"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        credential = CredentialSimple.from_dict(d.pop("credential"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        conversation_provider_list = cls(
            id=id,
            name=name,
            kind=kind,
            organization=organization,
            credential=credential,
            created_at=created_at,
            updated_at=updated_at,
        )

        conversation_provider_list.additional_properties = d
        return conversation_provider_list

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
