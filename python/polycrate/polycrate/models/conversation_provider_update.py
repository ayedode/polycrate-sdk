from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_provider_update_secrets_type_0 import ConversationProviderUpdateSecretsType0


T = TypeVar("T", bound="ConversationProviderUpdate")


@_attrs_define
class ConversationProviderUpdate:
    """Serializer for ConversationProvider updates.
    Following S3 pattern with restricted update fields.

        Attributes:
            id (UUID):
            credential (None | Unset | UUID): Credential for accessing the conversation provider
            meta (Any | Unset): Provider metadata as JSON object
            config (Any | Unset): Provider configuration as JSON object
            secrets (ConversationProviderUpdateSecretsType0 | None | Unset): Provider secrets as JSON object (encrypted in
                database)
    """

    id: UUID
    credential: None | Unset | UUID = UNSET
    meta: Any | Unset = UNSET
    config: Any | Unset = UNSET
    secrets: ConversationProviderUpdateSecretsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.conversation_provider_update_secrets_type_0 import (
            ConversationProviderUpdateSecretsType0,  # noqa: PLC0415
        )

        id = str(self.id)

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
        elif isinstance(self.secrets, ConversationProviderUpdateSecretsType0):
            secrets = self.secrets.to_dict()
        else:
            secrets = self.secrets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
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
        from ..models.conversation_provider_update_secrets_type_0 import (
            ConversationProviderUpdateSecretsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = UUID(d.pop("id"))

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

        def _parse_secrets(data: object) -> ConversationProviderUpdateSecretsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secrets_type_0 = ConversationProviderUpdateSecretsType0.from_dict(data)

                return secrets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConversationProviderUpdateSecretsType0 | None | Unset, data)

        secrets = _parse_secrets(d.pop("secrets", UNSET))

        conversation_provider_update = cls(
            id=id,
            credential=credential,
            meta=meta,
            config=config,
            secrets=secrets,
        )

        conversation_provider_update.additional_properties = d
        return conversation_provider_update

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
