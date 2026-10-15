from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.loadbalancer_instance_create_engine_version import (
    LoadbalancerInstanceCreateEngineVersion,
    check_loadbalancer_instance_create_engine_version,
)
from ..models.loadbalancer_instance_create_proxy_placement import (
    LoadbalancerInstanceCreateProxyPlacement,
    check_loadbalancer_instance_create_proxy_placement,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lbi_v2_spec import LbiV2Spec


T = TypeVar("T", bound="LoadbalancerInstanceCreate")


@_attrs_define
class LoadbalancerInstanceCreate:
    """Serializer for creating LoadBalancer instances.

    Accepts an optional `wizard_ports` field. When provided, the wizard logic
    from utils.py is applied: ports are validated, the HAProxy config is
    generated, and the internal K8s-format `ports` field is assembled — identical
    to what the UI wizard does. The `wizard_ports` field is write-only and not
    returned in the response.

        Attributes:
            id (UUID):
            workspace (UUID):
            organization (UUID):
            display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
                from the name.
            config (str | Unset): Load Balancer specific configuration (YAML/JSON)
            ports (Any | Unset): Port configuration: [{port: 80, name: 'port-80', protocol: 'TCP', target_port: 80}]
            consumer_meta (Any | Unset): Arbitrary metadata from the consumer of this LoadBalancer instance
            labels (Any | Unset):
            annotations (Any | Unset):
            resource_limits (Any | Unset): Optional HAProxy limit overrides: {cpu, memory}. Empty inherits SystemConfig.
            haproxy_defaults (Any | Unset): Optional HAProxy defaults overrides: {timeout_client_fin, timeout_server_fin,
                option_clitcpka, option_srvtcpka}. Empty inherits SystemConfig.
            engine_version (LoadbalancerInstanceCreateEngineVersion | Unset): 1 = HAProxy BlockRollout, 2 = Envoy Gateway
                API SSA. Spec 705.

                * `1` - HAProxy (v1)
                * `2` - Envoy / Gateway API (v2)
            spec (LbiV2Spec | None | Unset):
            proxy_placement (LoadbalancerInstanceCreateProxyPlacement | Unset): v2 placement. shared is rejected until a
                later spec.

                * `dedicated` - Dedicated
                * `shared` - Shared
    """

    id: UUID
    workspace: UUID
    organization: UUID
    display_name: None | str | Unset = UNSET
    config: str | Unset = UNSET
    ports: Any | Unset = UNSET
    consumer_meta: Any | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    resource_limits: Any | Unset = UNSET
    haproxy_defaults: Any | Unset = UNSET
    engine_version: LoadbalancerInstanceCreateEngineVersion | Unset = UNSET
    spec: LbiV2Spec | None | Unset = UNSET
    proxy_placement: LoadbalancerInstanceCreateProxyPlacement | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.lbi_v2_spec import LbiV2Spec  # noqa: PLC0415

        id = str(self.id)

        workspace = str(self.workspace)

        organization = str(self.organization)

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        config = self.config

        ports = self.ports

        consumer_meta = self.consumer_meta

        labels = self.labels

        annotations = self.annotations

        resource_limits = self.resource_limits

        haproxy_defaults = self.haproxy_defaults

        engine_version: int | Unset = UNSET
        if not isinstance(self.engine_version, Unset):
            engine_version = self.engine_version

        spec: dict[str, Any] | None | Unset
        if isinstance(self.spec, Unset):
            spec = UNSET
        elif isinstance(self.spec, LbiV2Spec):
            spec = self.spec.to_dict()
        else:
            spec = self.spec

        proxy_placement: str | Unset = UNSET
        if not isinstance(self.proxy_placement, Unset):
            proxy_placement = self.proxy_placement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workspace": workspace,
                "organization": organization,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if config is not UNSET:
            field_dict["config"] = config
        if ports is not UNSET:
            field_dict["ports"] = ports
        if consumer_meta is not UNSET:
            field_dict["consumer_meta"] = consumer_meta
        if labels is not UNSET:
            field_dict["labels"] = labels
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if resource_limits is not UNSET:
            field_dict["resource_limits"] = resource_limits
        if haproxy_defaults is not UNSET:
            field_dict["haproxy_defaults"] = haproxy_defaults
        if engine_version is not UNSET:
            field_dict["engine_version"] = engine_version
        if spec is not UNSET:
            field_dict["spec"] = spec
        if proxy_placement is not UNSET:
            field_dict["proxy_placement"] = proxy_placement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.lbi_v2_spec import LbiV2Spec  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        workspace = UUID(d.pop("workspace"))

        organization = UUID(d.pop("organization"))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        config = d.pop("config", UNSET)

        ports = d.pop("ports", UNSET)

        consumer_meta = d.pop("consumer_meta", UNSET)

        labels = d.pop("labels", UNSET)

        annotations = d.pop("annotations", UNSET)

        resource_limits = d.pop("resource_limits", UNSET)

        haproxy_defaults = d.pop("haproxy_defaults", UNSET)

        _engine_version = d.pop("engine_version", UNSET)
        engine_version: LoadbalancerInstanceCreateEngineVersion | Unset
        if isinstance(_engine_version, Unset):
            engine_version = UNSET
        else:
            engine_version = check_loadbalancer_instance_create_engine_version(_engine_version)

        def _parse_spec(data: object) -> LbiV2Spec | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                spec_type_1 = LbiV2Spec.from_dict(data)

                return spec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LbiV2Spec | None | Unset, data)

        spec = _parse_spec(d.pop("spec", UNSET))

        _proxy_placement = d.pop("proxy_placement", UNSET)
        proxy_placement: LoadbalancerInstanceCreateProxyPlacement | Unset
        if isinstance(_proxy_placement, Unset):
            proxy_placement = UNSET
        else:
            proxy_placement = check_loadbalancer_instance_create_proxy_placement(_proxy_placement)

        loadbalancer_instance_create = cls(
            id=id,
            workspace=workspace,
            organization=organization,
            display_name=display_name,
            config=config,
            ports=ports,
            consumer_meta=consumer_meta,
            labels=labels,
            annotations=annotations,
            resource_limits=resource_limits,
            haproxy_defaults=haproxy_defaults,
            engine_version=engine_version,
            spec=spec,
            proxy_placement=proxy_placement,
        )

        loadbalancer_instance_create.additional_properties = d
        return loadbalancer_instance_create

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
