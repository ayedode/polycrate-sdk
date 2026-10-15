from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_contact_list_effective_criticality_type_1 import (
    DomainContactListEffectiveCriticalityType1,
    check_domain_contact_list_effective_criticality_type_1,
)
from ..models.domain_contact_list_effective_criticality_type_2_type_1 import (
    DomainContactListEffectiveCriticalityType2Type1,
    check_domain_contact_list_effective_criticality_type_2_type_1,
)
from ..models.domain_contact_list_effective_criticality_type_3_type_1 import (
    DomainContactListEffectiveCriticalityType3Type1,
    check_domain_contact_list_effective_criticality_type_3_type_1,
)
from ..models.domain_contact_list_kind import DomainContactListKind, check_domain_contact_list_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_contact_list_active_condition_instances_item import (
        DomainContactListActiveConditionInstancesItem,
    )
    from ..models.domain_contact_list_created import DomainContactListCreated
    from ..models.domain_contact_list_organization_type_0 import DomainContactListOrganizationType0
    from ..models.domain_contact_list_workspace_type_0 import DomainContactListWorkspaceType0


T = TypeVar("T", bound="DomainContactList")


@_attrs_define
class DomainContactList:
    """Basis-Serializer für alle ManagedObject List-Endpoints.

    Liefert die generischen Felder die alle ManagedObjects teilen:
    - id: UUID
    - name: String-Repräsentation des Objects (__str__)
    - state: Object State
    - organization: Organization (id, slug, name)
    - workspace: Workspace (id, name) oder None
    - created: Kombifeld (created_at, created_at_humanized, created_at_display, created_by)

    Subclasses müssen:
    - model in Meta definieren
    - Zusätzliche model-spezifische Felder in Meta.fields hinzufügen

    Usage:
        class K8sClusterListSerializer(ManagedObjectListSerializer):
            class Meta(ManagedObjectListSerializer.Meta):
                model = K8sCluster
                fields = ManagedObjectListSerializer.Meta.fields + ['kubernetes_version', 'kind']

        Attributes:
            id (UUID):
            name (str): Gibt die bevorzugte UI-Anzeige (display_name) zurück.
            state (str):
            labels (Any):
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            condition_instance_count (int): Number of active ConditionInstances linked to this object (Spec 419).
                Uses prefetched data (_prefetched_active_conditions) when available to avoid N+1.
            active_condition_instances (list[DomainContactListActiveConditionInstancesItem]):
            organization (DomainContactListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (DomainContactListWorkspaceType0 | None):
            created (DomainContactListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (DomainContactListEffectiveCriticalityType1 |
                DomainContactListEffectiveCriticalityType2Type1 | DomainContactListEffectiveCriticalityType3Type1 | None):
            url (str): Gibt die absolute URL zum Object zurück.
            email (str):
            country (str): ISO-3166-1 alpha-2 country code.
            kind (DomainContactListKind | Unset): Person or legal organization. Controls required name fields.

                * `person` - Person
                * `organization` - Organization
            firstname (str | Unset):
            lastname (str | Unset):
            company_name (str | Unset):
    """

    id: UUID
    name: str
    state: str
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[DomainContactListActiveConditionInstancesItem]
    organization: DomainContactListOrganizationType0 | None
    organization_priority: bool
    workspace: DomainContactListWorkspaceType0 | None
    created: DomainContactListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: (
        DomainContactListEffectiveCriticalityType1
        | DomainContactListEffectiveCriticalityType2Type1
        | DomainContactListEffectiveCriticalityType3Type1
        | None
    )
    url: str
    email: str
    country: str
    kind: DomainContactListKind | Unset = UNSET
    firstname: str | Unset = UNSET
    lastname: str | Unset = UNSET
    company_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.domain_contact_list_organization_type_0 import DomainContactListOrganizationType0  # noqa: PLC0415
        from ..models.domain_contact_list_workspace_type_0 import DomainContactListWorkspaceType0  # noqa: PLC0415

        id = str(self.id)

        name = self.name

        state = self.state

        labels = self.labels

        conditions = self.conditions

        condition_instance_count = self.condition_instance_count

        active_condition_instances = []
        for active_condition_instances_item_data in self.active_condition_instances:
            active_condition_instances_item = active_condition_instances_item_data.to_dict()
            active_condition_instances.append(active_condition_instances_item)

        organization: dict[str, Any] | None
        if isinstance(self.organization, DomainContactListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, DomainContactListWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        created = self.created.to_dict()

        archived = self.archived

        reconciliation_running = self.reconciliation_running

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        elif isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        elif isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        url = self.url

        email = self.email

        country = self.country

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        firstname = self.firstname

        lastname = self.lastname

        company_name = self.company_name

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
                "email": email,
                "country": country,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if firstname is not UNSET:
            field_dict["firstname"] = firstname
        if lastname is not UNSET:
            field_dict["lastname"] = lastname
        if company_name is not UNSET:
            field_dict["company_name"] = company_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.domain_contact_list_active_condition_instances_item import (
            DomainContactListActiveConditionInstancesItem,  # noqa: PLC0415
        )
        from ..models.domain_contact_list_created import DomainContactListCreated  # noqa: PLC0415
        from ..models.domain_contact_list_organization_type_0 import DomainContactListOrganizationType0  # noqa: PLC0415
        from ..models.domain_contact_list_workspace_type_0 import DomainContactListWorkspaceType0  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        state = d.pop("state")

        labels = d.pop("labels")

        conditions = d.pop("conditions")

        condition_instance_count = d.pop("condition_instance_count")

        active_condition_instances = []
        _active_condition_instances = d.pop("active_condition_instances")
        for active_condition_instances_item_data in _active_condition_instances:
            active_condition_instances_item = DomainContactListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> DomainContactListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = DomainContactListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DomainContactListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> DomainContactListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = DomainContactListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DomainContactListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = DomainContactListCreated.from_dict(d.pop("created"))

        archived = d.pop("archived")

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_effective_criticality(
            data: object,
        ) -> (
            DomainContactListEffectiveCriticalityType1
            | DomainContactListEffectiveCriticalityType2Type1
            | DomainContactListEffectiveCriticalityType3Type1
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_1 = check_domain_contact_list_effective_criticality_type_1(data)

                return effective_criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_2_type_1 = check_domain_contact_list_effective_criticality_type_2_type_1(
                    data
                )

                return effective_criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_criticality_type_3_type_1 = check_domain_contact_list_effective_criticality_type_3_type_1(
                    data
                )

                return effective_criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                DomainContactListEffectiveCriticalityType1
                | DomainContactListEffectiveCriticalityType2Type1
                | DomainContactListEffectiveCriticalityType3Type1
                | None,
                data,
            )

        effective_criticality = _parse_effective_criticality(d.pop("effective_criticality"))

        url = d.pop("url")

        email = d.pop("email")

        country = d.pop("country")

        _kind = d.pop("kind", UNSET)
        kind: DomainContactListKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_domain_contact_list_kind(_kind)

        firstname = d.pop("firstname", UNSET)

        lastname = d.pop("lastname", UNSET)

        company_name = d.pop("company_name", UNSET)

        domain_contact_list = cls(
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
            email=email,
            country=country,
            kind=kind,
            firstname=firstname,
            lastname=lastname,
            company_name=company_name,
        )

        domain_contact_list.additional_properties = d
        return domain_contact_list

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
