from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadbalancerInstanceUpdate")


@_attrs_define
class LoadbalancerInstanceUpdate:
    """Serializer for updating LoadBalancer instances.

    Accepts an optional `wizard_ports` field. When provided, the wizard logic
    from utils.py is applied: the HAProxy config is regenerated and the internal
    K8s-format `ports` field is reassembled — identical to what perform_create
    does and what the UI wizard edit form does.

        Attributes:
            config (str | Unset): Load Balancer specific configuration (YAML/JSON)
            ports (Any | Unset): Port configuration: [{port: 80, name: 'port-80', protocol: 'TCP', target_port: 80}]
            labels (Any | Unset):
            annotations (Any | Unset):
            resource_limits (Any | Unset): Optional HAProxy limit overrides: {cpu, memory}. Empty inherits SystemConfig.
            haproxy_defaults (Any | Unset): Optional HAProxy defaults overrides: {timeout_client_fin, timeout_server_fin,
                option_clitcpka, option_srvtcpka}. Empty inherits SystemConfig.
    """

    config: str | Unset = UNSET
    ports: Any | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    resource_limits: Any | Unset = UNSET
    haproxy_defaults: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config

        ports = self.ports

        labels = self.labels

        annotations = self.annotations

        resource_limits = self.resource_limits

        haproxy_defaults = self.haproxy_defaults

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if ports is not UNSET:
            field_dict["ports"] = ports
        if labels is not UNSET:
            field_dict["labels"] = labels
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if resource_limits is not UNSET:
            field_dict["resource_limits"] = resource_limits
        if haproxy_defaults is not UNSET:
            field_dict["haproxy_defaults"] = haproxy_defaults

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config = d.pop("config", UNSET)

        ports = d.pop("ports", UNSET)

        labels = d.pop("labels", UNSET)

        annotations = d.pop("annotations", UNSET)

        resource_limits = d.pop("resource_limits", UNSET)

        haproxy_defaults = d.pop("haproxy_defaults", UNSET)

        loadbalancer_instance_update = cls(
            config=config,
            ports=ports,
            labels=labels,
            annotations=annotations,
            resource_limits=resource_limits,
            haproxy_defaults=haproxy_defaults,
        )

        loadbalancer_instance_update.additional_properties = d
        return loadbalancer_instance_update

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
