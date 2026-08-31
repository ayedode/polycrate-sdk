from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="S3CredentialWithSecrets")


@_attrs_define
class S3CredentialWithSecrets:
    """S3 Access Key including secrets.

    `access_key` maps to `api_user` (the RadosGW access key ID).
    `secret_key` maps to `api_key` (the RadosGW secret key).

    Spec 508: returned in the legacy list envelope (`data.credentials`) and in
    the create envelope (`data`). Callers that must avoid persisting secrets
    should discard them client-side after use.

        Attributes:
            id (UUID):
            name (str):
            description (None | str):
            api_user (None | str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            active (bool):
            metadata (Any):
            permissions (str):
            subuser_id (None | str):
            principal_arn (None | str):
            type_ (str):
            organization (None | UUID):
            access_key (None | str):
            secret_key (None | str):
    """

    id: UUID
    name: str
    description: None | str
    api_user: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    active: bool
    metadata: Any
    permissions: str
    subuser_id: None | str
    principal_arn: None | str
    type_: str
    organization: None | UUID
    access_key: None | str
    secret_key: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        description: None | str
        description = self.description

        api_user: None | str
        api_user = self.api_user

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        active = self.active

        metadata = self.metadata

        permissions = self.permissions

        subuser_id: None | str
        subuser_id = self.subuser_id

        principal_arn: None | str
        principal_arn = self.principal_arn

        type_ = self.type_

        organization: None | str
        if isinstance(self.organization, UUID):
            organization = str(self.organization)
        else:
            organization = self.organization

        access_key: None | str
        access_key = self.access_key

        secret_key: None | str
        secret_key = self.secret_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "api_user": api_user,
                "created_at": created_at,
                "updated_at": updated_at,
                "active": active,
                "metadata": metadata,
                "permissions": permissions,
                "subuser_id": subuser_id,
                "principal_arn": principal_arn,
                "type": type_,
                "organization": organization,
                "access_key": access_key,
                "secret_key": secret_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_api_user(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        api_user = _parse_api_user(d.pop("api_user"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        active = d.pop("active")

        metadata = d.pop("metadata")

        permissions = d.pop("permissions")

        def _parse_subuser_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subuser_id = _parse_subuser_id(d.pop("subuser_id"))

        def _parse_principal_arn(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        principal_arn = _parse_principal_arn(d.pop("principal_arn"))

        type_ = d.pop("type")

        def _parse_organization(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_type_0 = UUID(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_access_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        access_key = _parse_access_key(d.pop("access_key"))

        def _parse_secret_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        secret_key = _parse_secret_key(d.pop("secret_key"))

        s3_credential_with_secrets = cls(
            id=id,
            name=name,
            description=description,
            api_user=api_user,
            created_at=created_at,
            updated_at=updated_at,
            active=active,
            metadata=metadata,
            permissions=permissions,
            subuser_id=subuser_id,
            principal_arn=principal_arn,
            type_=type_,
            organization=organization,
            access_key=access_key,
            secret_key=secret_key,
        )

        s3_credential_with_secrets.additional_properties = d
        return s3_credential_with_secrets

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
