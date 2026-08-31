from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadbalancerInstanceCreateRequest")


@_attrs_define
class LoadbalancerInstanceCreateRequest:
    """Serializer for creating LoadBalancer instances.

    Accepts an optional `wizard_ports` field. When provided, the wizard logic
    from utils.py is applied: ports are validated, the HAProxy config is
    generated, and the internal K8s-format `ports` field is assembled — identical
    to what the UI wizard does. The `wizard_ports` field is write-only and not
    returned in the response.

        Attributes:
            workspace (UUID):
            organization (UUID):
            display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
                from the name.
            config (str | Unset): Load Balancer specific configuration (YAML/JSON)
            ports (Any | Unset): Port configuration: [{port: 80, name: 'port-80', protocol: 'TCP', target_port: 80}]
            wizard_ports (Any | Unset):
            consumer_meta (Any | Unset): Arbitrary metadata from the consumer of this LoadBalancer instance
            labels (Any | Unset):
            annotations (Any | Unset):
    """

    workspace: UUID
    organization: UUID
    display_name: None | str | Unset = UNSET
    config: str | Unset = UNSET
    ports: Any | Unset = UNSET
    wizard_ports: Any | Unset = UNSET
    consumer_meta: Any | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workspace = str(self.workspace)

        organization = str(self.organization)

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        config = self.config

        ports = self.ports

        wizard_ports = self.wizard_ports

        consumer_meta = self.consumer_meta

        labels = self.labels

        annotations = self.annotations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
        if wizard_ports is not UNSET:
            field_dict["wizard_ports"] = wizard_ports
        if consumer_meta is not UNSET:
            field_dict["consumer_meta"] = consumer_meta
        if labels is not UNSET:
            field_dict["labels"] = labels
        if annotations is not UNSET:
            field_dict["annotations"] = annotations

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("workspace", (None, str(self.workspace), "text/plain")))

        files.append(("organization", (None, str(self.organization), "text/plain")))

        if not isinstance(self.display_name, Unset):
            if isinstance(self.display_name, str):
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))
            else:
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))

        if not isinstance(self.config, Unset):
            files.append(("config", (None, str(self.config).encode(), "text/plain")))

        if not isinstance(self.ports, Unset):
            files.append(("ports", (None, str(self.ports).encode(), "text/plain")))

        if not isinstance(self.wizard_ports, Unset):
            files.append(("wizard_ports", (None, str(self.wizard_ports).encode(), "text/plain")))

        if not isinstance(self.consumer_meta, Unset):
            files.append(("consumer_meta", (None, str(self.consumer_meta).encode(), "text/plain")))

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

        wizard_ports = d.pop("wizard_ports", UNSET)

        consumer_meta = d.pop("consumer_meta", UNSET)

        labels = d.pop("labels", UNSET)

        annotations = d.pop("annotations", UNSET)

        loadbalancer_instance_create_request = cls(
            workspace=workspace,
            organization=organization,
            display_name=display_name,
            config=config,
            ports=ports,
            wizard_ports=wizard_ports,
            consumer_meta=consumer_meta,
            labels=labels,
            annotations=annotations,
        )

        loadbalancer_instance_create_request.additional_properties = d
        return loadbalancer_instance_create_request

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
