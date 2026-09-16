from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_group_kind_enum import ContactGroupKindEnum, check_contact_group_kind_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_group_maintainers_item import ContactGroupMaintainersItem
    from ..models.contact_group_membership import ContactGroupMembership
    from ..models.contact_group_owners_item import ContactGroupOwnersItem
    from ..models.organization import Organization


T = TypeVar("T", bound="ContactGroup")


@_attrs_define
class ContactGroup:
    """Full serializer for ContactGroup detail views and CRUD operations.

    Includes complete related object data and computed fields.

        Attributes:
            id (UUID):
            name (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            state (LastStateEnum): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            organization (Organization):
            member_count (int):
            owners (list[ContactGroupOwnersItem]):
            maintainers (list[ContactGroupMaintainersItem]):
            memberships (list[ContactGroupMembership]):
            kind (ContactGroupKindEnum | Unset): * `generic` - Generic
                * `dynamic` - Dynamic
            email (None | str | Unset): Group email address for notifications
            dynamic_rules (Any | Unset): Rules for dynamic group membership (JSON format)
            keycloak_group_id (None | str | Unset): Keycloak group ID for automatic synchronization
    """

    id: UUID
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    state: LastStateEnum
    conditions: Any
    organization: Organization
    member_count: int
    owners: list[ContactGroupOwnersItem]
    maintainers: list[ContactGroupMaintainersItem]
    memberships: list[ContactGroupMembership]
    kind: ContactGroupKindEnum | Unset = UNSET
    email: None | str | Unset = UNSET
    dynamic_rules: Any | Unset = UNSET
    keycloak_group_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        state: str = self.state

        conditions = self.conditions

        organization = self.organization.to_dict()

        member_count = self.member_count

        owners = []
        for owners_item_data in self.owners:
            owners_item = owners_item_data.to_dict()
            owners.append(owners_item)

        maintainers = []
        for maintainers_item_data in self.maintainers:
            maintainers_item = maintainers_item_data.to_dict()
            maintainers.append(maintainers_item)

        memberships = []
        for memberships_item_data in self.memberships:
            memberships_item = memberships_item_data.to_dict()
            memberships.append(memberships_item)

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        dynamic_rules = self.dynamic_rules

        keycloak_group_id: None | str | Unset
        if isinstance(self.keycloak_group_id, Unset):
            keycloak_group_id = UNSET
        else:
            keycloak_group_id = self.keycloak_group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
                "state": state,
                "conditions": conditions,
                "organization": organization,
                "member_count": member_count,
                "owners": owners,
                "maintainers": maintainers,
                "memberships": memberships,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if email is not UNSET:
            field_dict["email"] = email
        if dynamic_rules is not UNSET:
            field_dict["dynamic_rules"] = dynamic_rules
        if keycloak_group_id is not UNSET:
            field_dict["keycloak_group_id"] = keycloak_group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_group_maintainers_item import ContactGroupMaintainersItem  # noqa: PLC0415
        from ..models.contact_group_membership import ContactGroupMembership  # noqa: PLC0415
        from ..models.contact_group_owners_item import ContactGroupOwnersItem  # noqa: PLC0415
        from ..models.organization import Organization  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        state = check_last_state_enum(d.pop("state"))

        conditions = d.pop("conditions")

        organization = Organization.from_dict(d.pop("organization"))

        member_count = d.pop("member_count")

        owners = []
        _owners = d.pop("owners")
        for owners_item_data in _owners:
            owners_item = ContactGroupOwnersItem.from_dict(owners_item_data)

            owners.append(owners_item)

        maintainers = []
        _maintainers = d.pop("maintainers")
        for maintainers_item_data in _maintainers:
            maintainers_item = ContactGroupMaintainersItem.from_dict(maintainers_item_data)

            maintainers.append(maintainers_item)

        memberships = []
        _memberships = d.pop("memberships")
        for memberships_item_data in _memberships:
            memberships_item = ContactGroupMembership.from_dict(memberships_item_data)

            memberships.append(memberships_item)

        _kind = d.pop("kind", UNSET)
        kind: ContactGroupKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_contact_group_kind_enum(_kind)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        dynamic_rules = d.pop("dynamic_rules", UNSET)

        def _parse_keycloak_group_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keycloak_group_id = _parse_keycloak_group_id(d.pop("keycloak_group_id", UNSET))

        contact_group = cls(
            id=id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            state=state,
            conditions=conditions,
            organization=organization,
            member_count=member_count,
            owners=owners,
            maintainers=maintainers,
            memberships=memberships,
            kind=kind,
            email=email,
            dynamic_rules=dynamic_rules,
            keycloak_group_id=keycloak_group_id,
        )

        contact_group.additional_properties = d
        return contact_group

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
