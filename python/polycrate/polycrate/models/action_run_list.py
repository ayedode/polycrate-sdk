from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.action_run_status_enum import ActionRunStatusEnum, check_action_run_status_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.action_run_list_active_condition_instances_item import ActionRunListActiveConditionInstancesItem
    from ..models.action_run_list_created import ActionRunListCreated
    from ..models.action_run_list_created_by_user_type_0 import ActionRunListCreatedByUserType0
    from ..models.action_run_list_organization_type_0 import ActionRunListOrganizationType0
    from ..models.action_run_list_workspace_type_0 import ActionRunListWorkspaceType0
    from ..models.block_ref import BlockRef


T = TypeVar("T", bound="ActionRunList")


@_attrs_define
class ActionRunList:
    """ActionRun List serializer - erbt von ManagedObjectListSerializer.

    Generische Felder (von ManagedObjectListSerializer):
    - id, name, state, organization, workspace, created, reconciliation_running, url

    ActionRun-spezifische Felder:
    - status, action, block, started_at, finished_at, exit_code, created_by_user

    Verwendet BlockRefSerializer (nicht BlockSimpleSerializer) um teure
    JOIN-Ketten block→workspace→organization zu vermeiden.
    Per .specs/0.11.4/dynamic-table-v2.md

        Attributes:
            id (UUID):
            name (str): Gibt die bevorzugte UI-Anzeige (display_name) zurück.
            state (LastStateEnum): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            labels (Any):
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            condition_instance_count (int): Number of active ConditionInstances linked to this object (Spec 419).
                Uses prefetched data (_prefetched_active_conditions) when available to avoid N+1.
            active_condition_instances (list[ActionRunListActiveConditionInstancesItem]):
            organization (ActionRunListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (ActionRunListWorkspaceType0 | None):
            created (ActionRunListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            status (ActionRunStatusEnum): * `pending` - Pending
                * `running` - Running
                * `success` - Success
                * `failed` - Failed
                * `cancelled` - Cancelled
            action (None | str):
            block (BlockRef): Minimaler Block-Serializer für List-Contexts (z.B. ActionRunListSerializer).

                Enthält NUR id, name und url — keine nested workspace/organization.
                Eliminiert die teuren JOIN-Ketten block→workspace→organization aus List-Queries.
            started_at (datetime.datetime | None):
            finished_at (datetime.datetime | None):
            exit_code (int | None): Exit code of the action run
            created_by_user (ActionRunListCreatedByUserType0 | None):
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[ActionRunListActiveConditionInstancesItem]
    organization: ActionRunListOrganizationType0 | None
    organization_priority: bool
    workspace: ActionRunListWorkspaceType0 | None
    created: ActionRunListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    status: ActionRunStatusEnum
    action: None | str
    block: BlockRef
    started_at: datetime.datetime | None
    finished_at: datetime.datetime | None
    exit_code: int | None
    created_by_user: ActionRunListCreatedByUserType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_run_list_created_by_user_type_0 import ActionRunListCreatedByUserType0
        from ..models.action_run_list_organization_type_0 import ActionRunListOrganizationType0
        from ..models.action_run_list_workspace_type_0 import ActionRunListWorkspaceType0

        id = str(self.id)

        name = self.name

        state: str = self.state

        labels = self.labels

        conditions = self.conditions

        condition_instance_count = self.condition_instance_count

        active_condition_instances = []
        for active_condition_instances_item_data in self.active_condition_instances:
            active_condition_instances_item = active_condition_instances_item_data.to_dict()
            active_condition_instances.append(active_condition_instances_item)

        organization: dict[str, Any] | None
        if isinstance(self.organization, ActionRunListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, ActionRunListWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        created = self.created.to_dict()

        archived = self.archived

        reconciliation_running = self.reconciliation_running

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        status: str = self.status

        action: None | str
        action = self.action

        block = self.block.to_dict()

        started_at: None | str
        if isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        finished_at: None | str
        if isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        exit_code: int | None
        exit_code = self.exit_code

        created_by_user: dict[str, Any] | None
        if isinstance(self.created_by_user, ActionRunListCreatedByUserType0):
            created_by_user = self.created_by_user.to_dict()
        else:
            created_by_user = self.created_by_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "state": state,
                "labels": labels,
                "conditions": conditions,
                "condition_instance_count": condition_instance_count,
                "active_condition_instances": active_condition_instances,
                "organization": organization,
                "organization_priority": organization_priority,
                "workspace": workspace,
                "created": created,
                "archived": archived,
                "reconciliation_running": reconciliation_running,
                "effective_criticality": effective_criticality,
                "url": url,
                "status": status,
                "action": action,
                "block": block,
                "started_at": started_at,
                "finished_at": finished_at,
                "exit_code": exit_code,
                "created_by_user": created_by_user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_run_list_active_condition_instances_item import ActionRunListActiveConditionInstancesItem
        from ..models.action_run_list_created import ActionRunListCreated
        from ..models.action_run_list_created_by_user_type_0 import ActionRunListCreatedByUserType0
        from ..models.action_run_list_organization_type_0 import ActionRunListOrganizationType0
        from ..models.action_run_list_workspace_type_0 import ActionRunListWorkspaceType0
        from ..models.block_ref import BlockRef

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = check_last_state_enum(d.pop("state"))

        labels = d.pop("labels")

        conditions = d.pop("conditions")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = ActionRunListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> ActionRunListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = ActionRunListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionRunListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> ActionRunListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = ActionRunListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionRunListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = ActionRunListCreated.from_dict(d.pop("created"))

        archived = d.pop("archived")

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_effective_criticality(data: object) -> EffectiveCriticalityEnum | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_0 = check_effective_criticality_enum(data)

                return effective_criticality_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EffectiveCriticalityEnum | None, data)

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        url = d.pop("url")

        status = check_action_run_status_enum(d.pop("status"))

        def _parse_action(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        action = _parse_action(d.pop("action"))

        block = BlockRef.from_dict(d.pop("block"))

        def _parse_started_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = datetime.datetime.fromisoformat(data)

                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        started_at = _parse_started_at(d.pop("started_at"))

        def _parse_finished_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = datetime.datetime.fromisoformat(data)

                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        finished_at = _parse_finished_at(d.pop("finished_at"))

        def _parse_exit_code(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        exit_code = _parse_exit_code(d.pop("exit_code"))

        def _parse_created_by_user(data: object) -> ActionRunListCreatedByUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_by_user_type_0 = ActionRunListCreatedByUserType0.from_dict(data)

                return created_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionRunListCreatedByUserType0 | None, data)

        created_by_user = _parse_created_by_user(d.pop("created_by_user"))

        action_run_list = cls(
            id=id,
            name=name,
            state=state,
            labels=labels,
            conditions=conditions,
            condition_instance_count=condition_instance_count,
            active_condition_instances=active_condition_instances,
            organization=organization,
            organization_priority=organization_priority,
            workspace=workspace,
            created=created,
            archived=archived,
            reconciliation_running=reconciliation_running,
            effective_criticality=effective_criticality,
            url=url,
            status=status,
            action=action,
            block=block,
            started_at=started_at,
            finished_at=finished_at,
            exit_code=exit_code,
            created_by_user=created_by_user,
        )

        action_run_list.additional_properties = d
        return action_run_list

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
