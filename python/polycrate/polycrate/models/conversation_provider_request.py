from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.conversation_kind_enum import ConversationKindEnum, check_conversation_kind_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_provider_request_secrets_type_0 import ConversationProviderRequestSecretsType0


T = TypeVar("T", bound="ConversationProviderRequest")


@_attrs_define
class ConversationProviderRequest:
    """Full serializer for ConversationProvider detail views and CRUD operations.
    Following S3 pattern with comprehensive fields and validation.

        Attributes:
            meta (Any): Provider metadata as JSON object
            config (Any): Provider configuration as JSON object
            kind (ConversationKindEnum | Unset): * `generic` - Generic
                * `zammad` - Zammad
                * `slack` - Slack
                * `discord` - Discord
                * `telegram` - Telegram
                * `msteams` - Microsoft Teams
                * `email` - Email
            secrets (ConversationProviderRequestSecretsType0 | None | Unset): Provider secrets as JSON object (encrypted in
                database)
    """

    meta: Any
    config: Any
    kind: ConversationKindEnum | Unset = UNSET
    secrets: ConversationProviderRequestSecretsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.conversation_provider_request_secrets_type_0 import ConversationProviderRequestSecretsType0

        meta = self.meta

        config = self.config

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        secrets: dict[str, Any] | None | Unset
        if isinstance(self.secrets, Unset):
            secrets = UNSET
        elif isinstance(self.secrets, ConversationProviderRequestSecretsType0):
            secrets = self.secrets.to_dict()
        else:
            secrets = self.secrets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
                "config": config,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if secrets is not UNSET:
            field_dict["secrets"] = secrets

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        from ..models.conversation_provider_request_secrets_type_0 import ConversationProviderRequestSecretsType0

        files: types.RequestFiles = []

        files.append(("meta", (None, str(self.meta).encode(), "text/plain")))

        files.append(("config", (None, str(self.config).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.secrets, Unset):
            if isinstance(self.secrets, ConversationProviderRequestSecretsType0):
                files.append(("secrets", (None, json.dumps(self.secrets.to_dict()).encode(), "application/json")))
            else:
                files.append(("secrets", (None, str(self.secrets).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conversation_provider_request_secrets_type_0 import ConversationProviderRequestSecretsType0

        d = dict(src_dict)
        meta = d.pop("meta")

        config = d.pop("config")

        _kind = d.pop("kind", UNSET)
        kind: ConversationKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_conversation_kind_enum(_kind)

        def _parse_secrets(data: object) -> ConversationProviderRequestSecretsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secrets_type_0 = ConversationProviderRequestSecretsType0.from_dict(data)

                return secrets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConversationProviderRequestSecretsType0 | None | Unset, data)

        secrets = _parse_secrets(d.pop("secrets", UNSET))

        conversation_provider_request = cls(
            meta=meta,
            config=config,
            kind=kind,
            secrets=secrets,
        )

        conversation_provider_request.additional_properties = d
        return conversation_provider_request

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
