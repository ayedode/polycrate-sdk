from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.endpoint_kind_enum import EndpointKindEnum, check_endpoint_kind_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_endpoint_organization_type_0 import AgentEndpointOrganizationType0
    from ..models.agent_endpoint_workspace_type_0 import AgentEndpointWorkspaceType0
    from ..models.endpoint_spec import EndpointSpec


T = TypeVar("T", bound="AgentEndpoint")


@_attrs_define
class AgentEndpoint:
    """Optimized serializer for endpoints that agents need to monitor.

    Uses minimal nested serializers to avoid N+1 queries and reduce payload size.
    spec is annotated via _EndpointSpecField so drf-spectacular emits a typed schema,
    enabling a fully typed Spec struct in the generated Go API client.

        Attributes:
            id (UUID):
            name (str):
            kind (EndpointKindEnum): * `icmp` - ICMP Endpoint
                * `http` - HTTP Endpoint
                * `tcp` - TCP Endpoint
                * `dns` - DNS Endpoint
            remote_address (str):
            remote_port (int | None):
            workspace (AgentEndpointWorkspaceType0 | None):
            organization (AgentEndpointOrganizationType0 | None):
            spec (EndpointSpec | None | Unset):
    """

    id: UUID
    name: str
    kind: EndpointKindEnum
    remote_address: str
    remote_port: int | None
    workspace: AgentEndpointWorkspaceType0 | None
    organization: AgentEndpointOrganizationType0 | None
    spec: EndpointSpec | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_endpoint_organization_type_0 import AgentEndpointOrganizationType0
        from ..models.agent_endpoint_workspace_type_0 import AgentEndpointWorkspaceType0
        from ..models.endpoint_spec import EndpointSpec

        id = str(self.id)

        name = self.name

        kind: str = self.kind

        remote_address = self.remote_address

        remote_port: int | None
        remote_port = self.remote_port

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, AgentEndpointWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        organization: dict[str, Any] | None
        if isinstance(self.organization, AgentEndpointOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        spec: dict[str, Any] | None | Unset
        if isinstance(self.spec, Unset):
            spec = UNSET
        elif isinstance(self.spec, EndpointSpec):
            spec = self.spec.to_dict()
        else:
            spec = self.spec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "kind": kind,
                "remote_address": remote_address,
                "remote_port": remote_port,
                "workspace": workspace,
                "organization": organization,
            }
        )
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_endpoint_organization_type_0 import AgentEndpointOrganizationType0
        from ..models.agent_endpoint_workspace_type_0 import AgentEndpointWorkspaceType0
        from ..models.endpoint_spec import EndpointSpec

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        kind = check_endpoint_kind_enum(d.pop("kind"))

        remote_address = d.pop("remote_address")

        def _parse_remote_port(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        remote_port = _parse_remote_port(d.pop("remote_port"))

        def _parse_workspace(data: object) -> AgentEndpointWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = AgentEndpointWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentEndpointWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        def _parse_organization(data: object) -> AgentEndpointOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = AgentEndpointOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentEndpointOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_spec(data: object) -> EndpointSpec | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                spec_type_1 = EndpointSpec.from_dict(data)

                return spec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EndpointSpec | None | Unset, data)

        spec = _parse_spec(d.pop("spec", UNSET))

        agent_endpoint = cls(
            id=id,
            name=name,
            kind=kind,
            remote_address=remote_address,
            remote_port=remote_port,
            workspace=workspace,
            organization=organization,
            spec=spec,
        )

        agent_endpoint.additional_properties = d
        return agent_endpoint

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
