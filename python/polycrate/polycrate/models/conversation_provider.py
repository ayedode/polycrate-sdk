from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conversation_kind_enum import ConversationKindEnum, check_conversation_kind_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_list import ConversationList
    from ..models.conversation_provider_secrets_type_0 import ConversationProviderSecretsType0
    from ..models.credential import Credential
    from ..models.organization_simple import OrganizationSimple


T = TypeVar("T", bound="ConversationProvider")


@_attrs_define
class ConversationProvider:
    """Full serializer for ConversationProvider detail views and CRUD operations.
    Following S3 pattern with comprehensive fields and validation.

        Attributes:
            id (UUID):
            name (str):
            organization (OrganizationSimple): Simple Organization serializer for nested representations.

                Includes `url` field for direct navigation.
            credential (Credential): Full serializer for Credential detail views.
            conversations (list[ConversationList]):
            meta (Any): Provider metadata as JSON object
            config (Any): Provider configuration as JSON object
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            kind (ConversationKindEnum | Unset): * `generic` - Generic
                * `zammad` - Zammad
                * `slack` - Slack
                * `discord` - Discord
                * `telegram` - Telegram
                * `msteams` - Microsoft Teams
                * `email` - Email
            secrets (ConversationProviderSecretsType0 | None | Unset): Provider secrets as JSON object (encrypted in
                database)
    """

    id: UUID
    name: str
    organization: OrganizationSimple
    credential: Credential
    conversations: list[ConversationList]
    meta: Any
    config: Any
    created_at: datetime.datetime
    updated_at: datetime.datetime
    kind: ConversationKindEnum | Unset = UNSET
    secrets: ConversationProviderSecretsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.conversation_provider_secrets_type_0 import ConversationProviderSecretsType0

        id = str(self.id)

        name = self.name

        organization = self.organization.to_dict()

        credential = self.credential.to_dict()

        conversations = []
        for conversations_item_data in self.conversations:
            conversations_item = conversations_item_data.to_dict()
            conversations.append(conversations_item)

        meta = self.meta

        config = self.config

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        secrets: dict[str, Any] | None | Unset
        if isinstance(self.secrets, Unset):
            secrets = UNSET
        elif isinstance(self.secrets, ConversationProviderSecretsType0):
            secrets = self.secrets.to_dict()
        else:
            secrets = self.secrets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "organization": organization,
                "credential": credential,
                "conversations": conversations,
                "meta": meta,
                "config": config,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if secrets is not UNSET:
            field_dict["secrets"] = secrets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_list import ConversationList
        from ..models.conversation_provider_secrets_type_0 import ConversationProviderSecretsType0
        from ..models.credential import Credential
        from ..models.organization_simple import OrganizationSimple

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        credential = Credential.from_dict(d.pop("credential"))

        conversations = []
        _conversations = d.pop("conversations")
        for conversations_item_data in _conversations:
            conversations_item = ConversationList.from_dict(conversations_item_data)

            conversations.append(conversations_item)

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

        def _parse_secrets(data: object) -> ConversationProviderSecretsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secrets_type_0 = ConversationProviderSecretsType0.from_dict(data)

                return secrets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConversationProviderSecretsType0 | None | Unset, data)

        secrets = _parse_secrets(d.pop("secrets", UNSET))

        conversation_provider = cls(
            id=id,
            name=name,
            organization=organization,
            credential=credential,
            conversations=conversations,
            meta=meta,
            config=config,
            created_at=created_at,
            updated_at=updated_at,
            kind=kind,
            secrets=secrets,
        )

        conversation_provider.additional_properties = d
        return conversation_provider

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
