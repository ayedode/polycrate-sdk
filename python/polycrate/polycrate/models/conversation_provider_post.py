from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.conversation_kind_enum import ConversationKindEnum, check_conversation_kind_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_provider_post_secrets_type_0 import ConversationProviderPostSecretsType0


T = TypeVar("T", bound="ConversationProviderPost")


@_attrs_define
class ConversationProviderPost:
    """Serializer for ConversationProvider creation.
    Following S3 pattern with validation and create logic.

        Attributes:
            id (UUID):
            name (str):
            kind (ConversationKindEnum | Unset): * `generic` - Generic
                * `zammad` - Zammad
                * `slack` - Slack
                * `discord` - Discord
                * `telegram` - Telegram
                * `msteams` - Microsoft Teams
                * `email` - Email
            organization (None | Unset | UUID): Organization that owns this conversation provider (optional)
            credential (None | Unset | UUID): Credential for accessing the conversation provider
            meta (Any | Unset): Provider metadata as JSON object
            config (Any | Unset): Provider configuration as JSON object
            secrets (ConversationProviderPostSecretsType0 | None | Unset): Provider secrets as JSON object (encrypted in
                database)
    """

    id: UUID
    name: str
    kind: ConversationKindEnum | Unset = UNSET
    organization: None | Unset | UUID = UNSET
    credential: None | Unset | UUID = UNSET
    meta: Any | Unset = UNSET
    config: Any | Unset = UNSET
    secrets: ConversationProviderPostSecretsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.conversation_provider_post_secrets_type_0 import ConversationProviderPostSecretsType0

        id = str(self.id)

        name = self.name

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        organization: None | str | Unset
        if isinstance(self.organization, Unset):
            organization = UNSET
        elif isinstance(self.organization, UUID):
            organization = str(self.organization)
        else:
            organization = self.organization

        credential: None | str | Unset
        if isinstance(self.credential, Unset):
            credential = UNSET
        elif isinstance(self.credential, UUID):
            credential = str(self.credential)
        else:
            credential = self.credential

        meta = self.meta

        config = self.config

        secrets: dict[str, Any] | None | Unset
        if isinstance(self.secrets, Unset):
            secrets = UNSET
        elif isinstance(self.secrets, ConversationProviderPostSecretsType0):
            secrets = self.secrets.to_dict()
        else:
            secrets = self.secrets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if organization is not UNSET:
            field_dict["organization"] = organization
        if credential is not UNSET:
            field_dict["credential"] = credential
        if meta is not UNSET:
            field_dict["meta"] = meta
        if config is not UNSET:
            field_dict["config"] = config
        if secrets is not UNSET:
            field_dict["secrets"] = secrets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_provider_post_secrets_type_0 import ConversationProviderPostSecretsType0

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        _kind = d.pop("kind", UNSET)
        kind: ConversationKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_conversation_kind_enum(_kind)

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

        def _parse_credential(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credential_type_0 = UUID(data)

                return credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        credential = _parse_credential(d.pop("credential", UNSET))

        meta = d.pop("meta", UNSET)

        config = d.pop("config", UNSET)

        def _parse_secrets(data: object) -> ConversationProviderPostSecretsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secrets_type_0 = ConversationProviderPostSecretsType0.from_dict(data)

                return secrets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConversationProviderPostSecretsType0 | None | Unset, data)

        secrets = _parse_secrets(d.pop("secrets", UNSET))

        conversation_provider_post = cls(
            id=id,
            name=name,
            kind=kind,
            organization=organization,
            credential=credential,
            meta=meta,
            config=config,
            secrets=secrets,
        )

        conversation_provider_post.additional_properties = d
        return conversation_provider_post

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
