from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credential_update_request_secrets_type_0 import CredentialUpdateRequestSecretsType0


T = TypeVar("T", bound="CredentialUpdateRequest")


@_attrs_define
class CredentialUpdateRequest:
    """Serializer for updating credentials via API (microservice integration).
    Only allows updating credential data fields, not metadata.

        Attributes:
            api_endpoint (None | str | Unset):
            api_user (None | str | Unset):
            api_key (None | str | Unset):
            secrets (CredentialUpdateRequestSecretsType0 | None | Unset): Credential secrets as JSON object (encrypted in
                database)
            kubeconfig (None | str | Unset):
            ssh_private_key (None | str | Unset):
            ssh_public_key (None | str | Unset):
            metadata (Any | Unset):
    """

    api_endpoint: None | str | Unset = UNSET
    api_user: None | str | Unset = UNSET
    api_key: None | str | Unset = UNSET
    secrets: CredentialUpdateRequestSecretsType0 | None | Unset = UNSET
    kubeconfig: None | str | Unset = UNSET
    ssh_private_key: None | str | Unset = UNSET
    ssh_public_key: None | str | Unset = UNSET
    metadata: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.credential_update_request_secrets_type_0 import (
            CredentialUpdateRequestSecretsType0,  # noqa: PLC0415
        )

        api_endpoint: None | str | Unset
        if isinstance(self.api_endpoint, Unset):
            api_endpoint = UNSET
        else:
            api_endpoint = self.api_endpoint

        api_user: None | str | Unset
        if isinstance(self.api_user, Unset):
            api_user = UNSET
        else:
            api_user = self.api_user

        api_key: None | str | Unset
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        secrets: dict[str, Any] | None | Unset
        if isinstance(self.secrets, Unset):
            secrets = UNSET
        elif isinstance(self.secrets, CredentialUpdateRequestSecretsType0):
            secrets = self.secrets.to_dict()
        else:
            secrets = self.secrets

        kubeconfig: None | str | Unset
        if isinstance(self.kubeconfig, Unset):
            kubeconfig = UNSET
        else:
            kubeconfig = self.kubeconfig

        ssh_private_key: None | str | Unset
        if isinstance(self.ssh_private_key, Unset):
            ssh_private_key = UNSET
        else:
            ssh_private_key = self.ssh_private_key

        ssh_public_key: None | str | Unset
        if isinstance(self.ssh_public_key, Unset):
            ssh_public_key = UNSET
        else:
            ssh_public_key = self.ssh_public_key

        metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_endpoint is not UNSET:
            field_dict["api_endpoint"] = api_endpoint
        if api_user is not UNSET:
            field_dict["api_user"] = api_user
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if kubeconfig is not UNSET:
            field_dict["kubeconfig"] = kubeconfig
        if ssh_private_key is not UNSET:
            field_dict["ssh_private_key"] = ssh_private_key
        if ssh_public_key is not UNSET:
            field_dict["ssh_public_key"] = ssh_public_key
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        from ..models.credential_update_request_secrets_type_0 import (
            CredentialUpdateRequestSecretsType0,  # noqa: PLC0415
        )

        files: types.RequestFiles = []

        if not isinstance(self.api_endpoint, Unset):
            if isinstance(self.api_endpoint, str):
                files.append(("api_endpoint", (None, str(self.api_endpoint).encode(), "text/plain")))
            else:
                files.append(("api_endpoint", (None, str(self.api_endpoint).encode(), "text/plain")))

        if not isinstance(self.api_user, Unset):
            if isinstance(self.api_user, str):
                files.append(("api_user", (None, str(self.api_user).encode(), "text/plain")))
            else:
                files.append(("api_user", (None, str(self.api_user).encode(), "text/plain")))

        if not isinstance(self.api_key, Unset):
            if isinstance(self.api_key, str):
                files.append(("api_key", (None, str(self.api_key).encode(), "text/plain")))
            else:
                files.append(("api_key", (None, str(self.api_key).encode(), "text/plain")))

        if not isinstance(self.secrets, Unset):
            if isinstance(self.secrets, CredentialUpdateRequestSecretsType0):
                files.append(("secrets", (None, json.dumps(self.secrets.to_dict()).encode(), "application/json")))
            else:
                files.append(("secrets", (None, str(self.secrets).encode(), "text/plain")))

        if not isinstance(self.kubeconfig, Unset):
            if isinstance(self.kubeconfig, str):
                files.append(("kubeconfig", (None, str(self.kubeconfig).encode(), "text/plain")))
            else:
                files.append(("kubeconfig", (None, str(self.kubeconfig).encode(), "text/plain")))

        if not isinstance(self.ssh_private_key, Unset):
            if isinstance(self.ssh_private_key, str):
                files.append(("ssh_private_key", (None, str(self.ssh_private_key).encode(), "text/plain")))
            else:
                files.append(("ssh_private_key", (None, str(self.ssh_private_key).encode(), "text/plain")))

        if not isinstance(self.ssh_public_key, Unset):
            if isinstance(self.ssh_public_key, str):
                files.append(("ssh_public_key", (None, str(self.ssh_public_key).encode(), "text/plain")))
            else:
                files.append(("ssh_public_key", (None, str(self.ssh_public_key).encode(), "text/plain")))

        if not isinstance(self.metadata, Unset):
            files.append(("metadata", (None, str(self.metadata).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_update_request_secrets_type_0 import (
            CredentialUpdateRequestSecretsType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_api_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_endpoint = _parse_api_endpoint(d.pop("api_endpoint", UNSET))

        def _parse_api_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_user = _parse_api_user(d.pop("api_user", UNSET))

        def _parse_api_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))

        def _parse_secrets(data: object) -> CredentialUpdateRequestSecretsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                secrets_type_0 = CredentialUpdateRequestSecretsType0.from_dict(data)

                return secrets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CredentialUpdateRequestSecretsType0 | None | Unset, data)

        secrets = _parse_secrets(d.pop("secrets", UNSET))

        def _parse_kubeconfig(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        kubeconfig = _parse_kubeconfig(d.pop("kubeconfig", UNSET))

        def _parse_ssh_private_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssh_private_key = _parse_ssh_private_key(d.pop("ssh_private_key", UNSET))

        def _parse_ssh_public_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssh_public_key = _parse_ssh_public_key(d.pop("ssh_public_key", UNSET))

        metadata = d.pop("metadata", UNSET)

        credential_update_request = cls(
            api_endpoint=api_endpoint,
            api_user=api_user,
            api_key=api_key,
            secrets=secrets,
            kubeconfig=kubeconfig,
            ssh_private_key=ssh_private_key,
            ssh_public_key=ssh_public_key,
            metadata=metadata,
        )

        credential_update_request.additional_properties = d
        return credential_update_request

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
