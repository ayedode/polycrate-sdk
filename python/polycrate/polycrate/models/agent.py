from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_kind_enum import AgentKindEnum, check_agent_kind_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.organization_simple import OrganizationSimple
    from ..models.pop_simple import PopSimple
    from ..models.workspace_simple import WorkspaceSimple


T = TypeVar("T", bound="Agent")


@_attrs_define
class Agent:
    """Agent Detail serializer - Full details for API responses.

    Attributes:
        id (UUID):
        name (str):
        state (LastStateEnum): * `OK` - Ok
            * `WARNING` - Warning
            * `CRITICAL` - Critical
            * `READY` - Ready
            * `DEGRADED` - Degraded
            * `DOWN` - Down
        organization (OrganizationSimple): Simple Organization serializer for nested representations.

            Includes `url` field for direct navigation.
        workspace (WorkspaceSimple):
        kind (AgentKindEnum): * `agent` - Agent
            * `operator` - Operator
        version (None | str): Version of the agent software
        is_active (bool): Whether this agent is considered active
        last_seen (datetime.datetime | None): Last time this agent called the API
        reported_agent_id (None | str): Agent-reported unique identifier for distinguishing multiple agents per
            workspace
        source_pop (PopSimple): Simple serializer for embedding Pop in other serializers.
        k8s_app (None | UUID): K8sApp that deploys this operator agent
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        url (str):
        icon_url (None | str):
    """

    id: UUID
    name: str
    state: LastStateEnum
    organization: OrganizationSimple
    workspace: WorkspaceSimple
    kind: AgentKindEnum
    version: None | str
    is_active: bool
    last_seen: datetime.datetime | None
    reported_agent_id: None | str
    source_pop: PopSimple
    k8s_app: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    url: str
    icon_url: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        state: str = self.state

        organization = self.organization.to_dict()

        workspace = self.workspace.to_dict()

        kind: str = self.kind

        version: None | str
        version = self.version

        is_active = self.is_active

        last_seen: None | str
        if isinstance(self.last_seen, datetime.datetime):
            last_seen = self.last_seen.isoformat()
        else:
            last_seen = self.last_seen

        reported_agent_id: None | str
        reported_agent_id = self.reported_agent_id

        source_pop = self.source_pop.to_dict()

        k8s_app: None | str
        if isinstance(self.k8s_app, UUID):
            k8s_app = str(self.k8s_app)
        else:
            k8s_app = self.k8s_app

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        url = self.url

        icon_url: None | str
        icon_url = self.icon_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "organization": organization,
                "workspace": workspace,
                "kind": kind,
                "version": version,
                "is_active": is_active,
                "last_seen": last_seen,
                "reported_agent_id": reported_agent_id,
                "source_pop": source_pop,
                "k8s_app": k8s_app,
                "created_at": created_at,
                "updated_at": updated_at,
                "url": url,
                "icon_url": icon_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_simple import OrganizationSimple  # noqa: PLC0415
        from ..models.pop_simple import PopSimple  # noqa: PLC0415
        from ..models.workspace_simple import WorkspaceSimple  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_last_state_enum(d.pop("state"))

        organization = OrganizationSimple.from_dict(d.pop("organization"))

        workspace = WorkspaceSimple.from_dict(d.pop("workspace"))

        kind = check_agent_kind_enum(d.pop("kind"))

        def _parse_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        version = _parse_version(d.pop("version"))

        is_active = d.pop("is_active")

        def _parse_last_seen(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_seen_type_0 = datetime.datetime.fromisoformat(data)

                return last_seen_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_seen = _parse_last_seen(d.pop("last_seen"))

        def _parse_reported_agent_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reported_agent_id = _parse_reported_agent_id(d.pop("reported_agent_id"))

        source_pop = PopSimple.from_dict(d.pop("source_pop"))

        def _parse_k8s_app(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                k8s_app_type_0 = UUID(data)

                return k8s_app_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        k8s_app = _parse_k8s_app(d.pop("k8s_app"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        url = d.pop("url")

        def _parse_icon_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        icon_url = _parse_icon_url(d.pop("icon_url"))

        agent = cls(
            id=id,
            name=name,
            state=state,
            organization=organization,
            workspace=workspace,
            kind=kind,
            version=version,
            is_active=is_active,
            last_seen=last_seen,
            reported_agent_id=reported_agent_id,
            source_pop=source_pop,
            k8s_app=k8s_app,
            created_at=created_at,
            updated_at=updated_at,
            url=url,
            icon_url=icon_url,
        )

        agent.additional_properties = d
        return agent

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
