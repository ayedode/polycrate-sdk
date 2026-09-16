from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_provider_update_request_secrets_type_0 import (
        ConversationProviderUpdateRequestSecretsType0,
    )


T = TypeVar("T", bound="ConversationProviderUpdateRequest")


@_attrs_define
class ConversationProviderUpdateRequest:
    """Serializer for ConversationProvider updates.
    Following S3 pattern with restricted update fields.

        Attributes:
            credential (None | Unset | UUID): Credential for accessing the conversation provider
            meta (Any | Unset): Provider metadata as JSON object
            config (Any | Unset): Provider configuration as JSON object
            secrets (ConversationProviderUpdateRequestSecretsType0 | None | Unset): Provider secrets as JSON object
                (encrypted in database)
    """

    credential: None | Unset | UUID = UNSET
    meta: Any | Unset = UNSET
    config: Any | Unset = UNSET
    secrets: ConversationProviderUpdateRequestSecretsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.conversation_provider_update_request_secrets_type_0 import (
            ConversationProviderUpdateRequestSecretsType0,  # noqa: PLC0415
        )

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
        elif isinstance(self.secrets, ConversationProviderUpdateRequestSecretsType0):
            secrets = self.secrets.to_dict()
        else:
            secrets = self.secrets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if credential is not UNSET:
            field_dict["credential"] = credential
        if meta is not UNSET:
            field_dict["meta"] = meta
        if config is not UNSET:
            field_dict["config"] = config
        if secrets is not UNSET:
            field_dict["secrets"] = secrets

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        from ..models.conversation_provider_update_request_secrets_type_0 import (
            ConversationProviderUpdateRequestSecretsType0,  # noqa: PLC0415
        )

        files: types.RequestFiles = []

        if not isinstance(self.credential, Unset):
            if isinstance(self.credential, UUID):
                files.append(("credential", (None, str(self.credential), "text/plain")))
            else:
                files.append(("credential", (None, str(self.credential).encode(), "text/plain")))

        if not isinstance(self.meta, Unset):
            files.append(("meta", (None, str(self.meta).encode(), "text/plain")))

        if not isinstance(self.config, Unset):
            files.append(("config", (None, str(self.config).encode(), "text/plain")))

        if not isinstance(self.secrets, Unset):
            if isinstance(self.secrets, ConversationProviderUpdateRequestSecretsType0):
                files.append(("secrets", (None, json.dumps(self.secrets.to_dict()).encode(), "application/json")))
            else:
                files.append(("secrets", (None, str(self.secrets).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_provider_update_request_secrets_type_0 import (
            ConversationProviderUpdateRequestSecretsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

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

        def _parse_secrets(data: object) -> ConversationProviderUpdateRequestSecretsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secrets_type_0 = ConversationProviderUpdateRequestSecretsType0.from_dict(data)

                return secrets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConversationProviderUpdateRequestSecretsType0 | None | Unset, data)

        secrets = _parse_secrets(d.pop("secrets", UNSET))

        conversation_provider_update_request = cls(
            credential=credential,
            meta=meta,
            config=config,
            secrets=secrets,
        )

        conversation_provider_update_request.additional_properties = d
        return conversation_provider_update_request

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
