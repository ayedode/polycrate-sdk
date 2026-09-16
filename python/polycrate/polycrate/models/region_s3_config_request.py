from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.region_s3_config_kind_enum import RegionS3ConfigKindEnum, check_region_s3_config_kind_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.region_s3_config_request_cluster_config import RegionS3ConfigRequestClusterConfig


T = TypeVar("T", bound="RegionS3ConfigRequest")


@_attrs_define
class RegionS3ConfigRequest:
    """
    Attributes:
        kind (RegionS3ConfigKindEnum | Unset): * `rook-ceph` - rook-ceph
            * `minio` - minio Default: 'rook-ceph'.
        endpoint (None | str | Unset):
        endpoint_secure (bool | Unset):  Default: True.
        admin_endpoint (None | str | Unset):
        admin_endpoint_secure (bool | Unset):  Default: True.
        region (None | str | Unset):
        namespace (None | str | Unset): Kubernetes namespace (rook-ceph default: 'rook-ceph')
        credential (None | Unset | UUID):
        default_product (None | Unset | UUID):
        cluster_config (RegionS3ConfigRequestClusterConfig | Unset):
        allow_new_buckets (bool | Unset):  Default: True.
        active (bool | Unset):  Default: False.
        include_in_cost_statement (bool | Unset):  Default: True.
    """

    kind: RegionS3ConfigKindEnum | Unset = "rook-ceph"
    endpoint: None | str | Unset = UNSET
    endpoint_secure: bool | Unset = True
    admin_endpoint: None | str | Unset = UNSET
    admin_endpoint_secure: bool | Unset = True
    region: None | str | Unset = UNSET
    namespace: None | str | Unset = UNSET
    credential: None | Unset | UUID = UNSET
    default_product: None | Unset | UUID = UNSET
    cluster_config: RegionS3ConfigRequestClusterConfig | Unset = UNSET
    allow_new_buckets: bool | Unset = True
    active: bool | Unset = False
    include_in_cost_statement: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        endpoint: None | str | Unset
        if isinstance(self.endpoint, Unset):
            endpoint = UNSET
        else:
            endpoint = self.endpoint

        endpoint_secure = self.endpoint_secure

        admin_endpoint: None | str | Unset
        if isinstance(self.admin_endpoint, Unset):
            admin_endpoint = UNSET
        else:
            admin_endpoint = self.admin_endpoint

        admin_endpoint_secure = self.admin_endpoint_secure

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        namespace: None | str | Unset
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        credential: None | str | Unset
        if isinstance(self.credential, Unset):
            credential = UNSET
        elif isinstance(self.credential, UUID):
            credential = str(self.credential)
        else:
            credential = self.credential

        default_product: None | str | Unset
        if isinstance(self.default_product, Unset):
            default_product = UNSET
        elif isinstance(self.default_product, UUID):
            default_product = str(self.default_product)
        else:
            default_product = self.default_product

        cluster_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cluster_config, Unset):
            cluster_config = self.cluster_config.to_dict()

        allow_new_buckets = self.allow_new_buckets

        active = self.active

        include_in_cost_statement = self.include_in_cost_statement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if endpoint_secure is not UNSET:
            field_dict["endpoint_secure"] = endpoint_secure
        if admin_endpoint is not UNSET:
            field_dict["admin_endpoint"] = admin_endpoint
        if admin_endpoint_secure is not UNSET:
            field_dict["admin_endpoint_secure"] = admin_endpoint_secure
        if region is not UNSET:
            field_dict["region"] = region
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if credential is not UNSET:
            field_dict["credential"] = credential
        if default_product is not UNSET:
            field_dict["default_product"] = default_product
        if cluster_config is not UNSET:
            field_dict["cluster_config"] = cluster_config
        if allow_new_buckets is not UNSET:
            field_dict["allow_new_buckets"] = allow_new_buckets
        if active is not UNSET:
            field_dict["active"] = active
        if include_in_cost_statement is not UNSET:
            field_dict["include_in_cost_statement"] = include_in_cost_statement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.region_s3_config_request_cluster_config import RegionS3ConfigRequestClusterConfig  # noqa: PLC0415

        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: RegionS3ConfigKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_region_s3_config_kind_enum(_kind)

        def _parse_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        endpoint = _parse_endpoint(d.pop("endpoint", UNSET))

        endpoint_secure = d.pop("endpoint_secure", UNSET)

        def _parse_admin_endpoint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        admin_endpoint = _parse_admin_endpoint(d.pop("admin_endpoint", UNSET))

        admin_endpoint_secure = d.pop("admin_endpoint_secure", UNSET)

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_namespace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

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

        def _parse_default_product(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_product_type_0 = UUID(data)

                return default_product_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        default_product = _parse_default_product(d.pop("default_product", UNSET))

        _cluster_config = d.pop("cluster_config", UNSET)
        cluster_config: RegionS3ConfigRequestClusterConfig | Unset
        if isinstance(_cluster_config, Unset):
            cluster_config = UNSET
        else:
            cluster_config = RegionS3ConfigRequestClusterConfig.from_dict(_cluster_config)

        allow_new_buckets = d.pop("allow_new_buckets", UNSET)

        active = d.pop("active", UNSET)

        include_in_cost_statement = d.pop("include_in_cost_statement", UNSET)

        region_s3_config_request = cls(
            kind=kind,
            endpoint=endpoint,
            endpoint_secure=endpoint_secure,
            admin_endpoint=admin_endpoint,
            admin_endpoint_secure=admin_endpoint_secure,
            region=region,
            namespace=namespace,
            credential=credential,
            default_product=default_product,
            cluster_config=cluster_config,
            allow_new_buckets=allow_new_buckets,
            active=active,
            include_in_cost_statement=include_in_cost_statement,
        )

        region_s3_config_request.additional_properties = d
        return region_s3_config_request

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
