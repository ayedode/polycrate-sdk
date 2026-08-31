from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadbalancerInstanceUpdateRequest")


@_attrs_define
class LoadbalancerInstanceUpdateRequest:
    """Serializer for updating LoadBalancer instances.

    Accepts an optional `wizard_ports` field. When provided, the wizard logic
    from utils.py is applied: the HAProxy config is regenerated and the internal
    K8s-format `ports` field is reassembled — identical to what perform_create
    does and what the UI wizard edit form does.

        Attributes:
            config (str | Unset): Load Balancer specific configuration (YAML/JSON)
            ports (Any | Unset): Port configuration: [{port: 80, name: 'port-80', protocol: 'TCP', target_port: 80}]
            wizard_ports (Any | Unset):
            labels (Any | Unset):
            annotations (Any | Unset):
    """

    config: str | Unset = UNSET
    ports: Any | Unset = UNSET
    wizard_ports: Any | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config

        ports = self.ports

        wizard_ports = self.wizard_ports

        labels = self.labels

        annotations = self.annotations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if ports is not UNSET:
            field_dict["ports"] = ports
        if wizard_ports is not UNSET:
            field_dict["wizard_ports"] = wizard_ports
        if labels is not UNSET:
            field_dict["labels"] = labels
        if annotations is not UNSET:
            field_dict["annotations"] = annotations

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.config, Unset):
            files.append(("config", (None, str(self.config).encode(), "text/plain")))

        if not isinstance(self.ports, Unset):
            files.append(("ports", (None, str(self.ports).encode(), "text/plain")))

        if not isinstance(self.wizard_ports, Unset):
            files.append(("wizard_ports", (None, str(self.wizard_ports).encode(), "text/plain")))

        if not isinstance(self.labels, Unset):
            files.append(("labels", (None, str(self.labels).encode(), "text/plain")))

        if not isinstance(self.annotations, Unset):
            files.append(("annotations", (None, str(self.annotations).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config = d.pop("config", UNSET)

        ports = d.pop("ports", UNSET)

        wizard_ports = d.pop("wizard_ports", UNSET)

        labels = d.pop("labels", UNSET)

        annotations = d.pop("annotations", UNSET)

        loadbalancer_instance_update_request = cls(
            config=config,
            ports=ports,
            wizard_ports=wizard_ports,
            labels=labels,
            annotations=annotations,
        )

        loadbalancer_instance_update_request.additional_properties = d
        return loadbalancer_instance_update_request

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
