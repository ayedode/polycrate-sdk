from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_role_enum import ContactRoleEnum, check_contact_role_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum

if TYPE_CHECKING:
    from ..models.contact_list_active_condition_instances_item import ContactListActiveConditionInstancesItem
    from ..models.contact_list_created import ContactListCreated
    from ..models.contact_list_organization_type_0 import ContactListOrganizationType0
    from ..models.contact_list_workspace_type_0 import ContactListWorkspaceType0


T = TypeVar("T", bound="ContactList")


@_attrs_define
class ContactList:
    """Contact List serializer - erbt von ManagedObjectListSerializer.

    Generische Felder (von ManagedObjectListSerializer):
    - id, name, state, organization, workspace, created_at, reconciliation_running, url

    Contact-spezifische Felder:
    - full_name, email, phone, is_maintenance_contact, is_billing_contact

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
            active_condition_instances (list[ContactListActiveConditionInstancesItem]):
            organization (ContactListOrganizationType0 | None):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (ContactListWorkspaceType0 | None):
            created (ContactListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            full_name (str): Get formatted full name.
            email (str): Email address of the contact
            phone (None | str): Phone number of the contact
            contact_role (ContactRoleEnum): * `developer` - Developer
                * `admin` - Admin
                * `billing` - Billing
                * `viewer` - Viewer
            is_maintenance_contact (bool): Whether this contact should receive maintenance notifications
            is_billing_contact (bool): Whether this contact should receive billing notifications
            keycloak_user_id (None | str): Keycloak user ID for automatic synchronization
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[ContactListActiveConditionInstancesItem]
    organization: ContactListOrganizationType0 | None
    organization_priority: bool
    workspace: ContactListWorkspaceType0 | None
    created: ContactListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    full_name: str
    email: str
    phone: None | str
    contact_role: ContactRoleEnum
    is_maintenance_contact: bool
    is_billing_contact: bool
    keycloak_user_id: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.contact_list_organization_type_0 import ContactListOrganizationType0
        from ..models.contact_list_workspace_type_0 import ContactListWorkspaceType0

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
        if isinstance(self.organization, ContactListOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        organization_priority = self.organization_priority

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, ContactListWorkspaceType0):
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

        full_name = self.full_name

        email = self.email

        phone: None | str
        phone = self.phone

        contact_role: str = self.contact_role

        is_maintenance_contact = self.is_maintenance_contact

        is_billing_contact = self.is_billing_contact

        keycloak_user_id: None | str
        keycloak_user_id = self.keycloak_user_id

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
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "contact_role": contact_role,
                "is_maintenance_contact": is_maintenance_contact,
                "is_billing_contact": is_billing_contact,
                "keycloak_user_id": keycloak_user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_list_active_condition_instances_item import ContactListActiveConditionInstancesItem
        from ..models.contact_list_created import ContactListCreated
        from ..models.contact_list_organization_type_0 import ContactListOrganizationType0
        from ..models.contact_list_workspace_type_0 import ContactListWorkspaceType0

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
            active_condition_instances_item = ContactListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> ContactListOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = ContactListOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactListOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> ContactListWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = ContactListWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContactListWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = ContactListCreated.from_dict(d.pop("created"))

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

        full_name = d.pop("full_name")

        email = d.pop("email")

        def _parse_phone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        phone = _parse_phone(d.pop("phone"))

        contact_role = check_contact_role_enum(d.pop("contact_role"))

        is_maintenance_contact = d.pop("is_maintenance_contact")

        is_billing_contact = d.pop("is_billing_contact")

        def _parse_keycloak_user_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        keycloak_user_id = _parse_keycloak_user_id(d.pop("keycloak_user_id"))

        contact_list = cls(
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
            full_name=full_name,
            email=email,
            phone=phone,
            contact_role=contact_role,
            is_maintenance_contact=is_maintenance_contact,
            is_billing_contact=is_billing_contact,
            keycloak_user_id=keycloak_user_id,
        )

        contact_list.additional_properties = d
        return contact_list

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
