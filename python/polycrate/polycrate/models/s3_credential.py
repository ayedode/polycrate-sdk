from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="S3Credential")


@_attrs_define
class S3Credential:
    """S3 Access Key metadata — no secrets.

    Additional access keys (type=additional) are only supported for rook-ceph
    (RadosGW) clusters. MinIO clusters do not support sub-user management;
    the credentials/create endpoint returns 400 for MinIO buckets.

    The `active` field is inherited from ManagedObject and has no semantic
    meaning for S3 access keys — do not use it to display key status.

    Spec 629: `principal_arn` is a computed Ceph/RGW IAM principal for bucket
    policies (no tenant). Consumers assemble policies themselves.

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

        s3_credential = cls(
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
        )

        s3_credential.additional_properties = d
        return s3_credential

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
