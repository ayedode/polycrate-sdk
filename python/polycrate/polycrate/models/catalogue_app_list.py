from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artifact_package_catalogue import ArtifactPackageCatalogue
    from ..models.catalogue_app_list_active_condition_instances_item import CatalogueAppListActiveConditionInstancesItem
    from ..models.catalogue_app_list_created import CatalogueAppListCreated
    from ..models.catalogue_app_list_latest_block_type_0 import CatalogueAppListLatestBlockType0
    from ..models.product_simple import ProductSimple


T = TypeVar("T", bound="CatalogueAppList")


@_attrs_define
class CatalogueAppList:
    """List serializer for CatalogueApp - V2 Dynamic Tables.
    Includes nested ArtifactPackage info and computed fields.

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
            active_condition_instances (list[CatalogueAppListActiveConditionInstancesItem]):
            organization (None | str):
            organization_priority (bool): True when the object's organization has priority=True.
            workspace (None | str):
            created (CatalogueAppListCreated):
            archived (bool): Archived objects are not shown in the UI and are not managed by the API.
            reconciliation_running (bool):
            effective_criticality (EffectiveCriticalityEnum | None):
            url (str): Gibt die absolute URL zum Object zurück.
            serial_number (int): Serial number from app catalogue (S/N)
            upstream_outdated (bool):
            artifact_package (ArtifactPackageCatalogue): Rich ArtifactPackage serializer for CatalogueApp / catalogue
                context.

                Uses ``ArtifactDerivedFieldsMixin`` to transparently expose metadata
                (version, license, changelog, readme …) from the latest Artifact of
                the package - or from a specifically requested one when
                ``_artifact_override`` is set in the serializer context.

                Per .specs/0.12.0/catalogue-app.md
            dependency_count (int):
            screenshot_url (str):
            price_monthly (str):
            product_regular (ProductSimple): Compact serializer for embedding Product as FK reference.
            product_ha (ProductSimple): Compact serializer for embedding Product as FK reference.
            latest_block (CatalogueAppListLatestBlockType0 | None):
            claim (str | Unset): Short marketing claim (mapped from Baserow 'info')
            short_description (None | str | Unset): What is this app? (mapped from Baserow 'what_is')
            draft (bool | Unset): Draft apps are not visible in the public catalogue
            is_new (bool | Unset): Highlight as new app in the catalogue
            supports_ha (bool | Unset): Whether HA (zero-downtime) deployment mode is supported for this app. Mirrors
                block.SupportsHA (CLI YAML: supports_ha).
            registry_url (str | Unset): OCI registry URL for this app (e.g. cargo.ayedo.cloud/ayedo/k8s/n8n). Used to match
                template blocks by their content_url prefix.
            releases_url (None | str | Unset): GitHub releases page or API URL (preferred upstream source).
            git_repository_url (None | str | Unset): GitHub repository URL; releases derived when releases_url is empty.
            tracked_app_version (None | str | Unset): Packaged app version tracked by ayedo (from Hub/block sync or manual).
            latest_upstream_version (None | str | Unset): Latest stable upstream version (denormalized from app-release
                notes).
            upstream_checked_at (datetime.datetime | None | Unset): Timestamp of the last upstream release sync.
    """

    id: UUID
    name: str
    state: LastStateEnum
    labels: Any
    conditions: Any
    condition_instance_count: int
    active_condition_instances: list[CatalogueAppListActiveConditionInstancesItem]
    organization: None | str
    organization_priority: bool
    workspace: None | str
    created: CatalogueAppListCreated
    archived: bool
    reconciliation_running: bool
    effective_criticality: EffectiveCriticalityEnum | None
    url: str
    serial_number: int
    upstream_outdated: bool
    artifact_package: ArtifactPackageCatalogue
    dependency_count: int
    screenshot_url: str
    price_monthly: str
    product_regular: ProductSimple
    product_ha: ProductSimple
    latest_block: CatalogueAppListLatestBlockType0 | None
    claim: str | Unset = UNSET
    short_description: None | str | Unset = UNSET
    draft: bool | Unset = UNSET
    is_new: bool | Unset = UNSET
    supports_ha: bool | Unset = UNSET
    registry_url: str | Unset = UNSET
    releases_url: None | str | Unset = UNSET
    git_repository_url: None | str | Unset = UNSET
    tracked_app_version: None | str | Unset = UNSET
    latest_upstream_version: None | str | Unset = UNSET
    upstream_checked_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.catalogue_app_list_latest_block_type_0 import CatalogueAppListLatestBlockType0

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

        organization: None | str
        organization = self.organization

        organization_priority = self.organization_priority

        workspace: None | str
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

        serial_number = self.serial_number

        upstream_outdated = self.upstream_outdated

        artifact_package = self.artifact_package.to_dict()

        dependency_count = self.dependency_count

        screenshot_url = self.screenshot_url

        price_monthly = self.price_monthly

        product_regular = self.product_regular.to_dict()

        product_ha = self.product_ha.to_dict()

        latest_block: dict[str, Any] | None
        if isinstance(self.latest_block, CatalogueAppListLatestBlockType0):
            latest_block = self.latest_block.to_dict()
        else:
            latest_block = self.latest_block

        claim = self.claim

        short_description: None | str | Unset
        if isinstance(self.short_description, Unset):
            short_description = UNSET
        else:
            short_description = self.short_description

        draft = self.draft

        is_new = self.is_new

        supports_ha = self.supports_ha

        registry_url = self.registry_url

        releases_url: None | str | Unset
        if isinstance(self.releases_url, Unset):
            releases_url = UNSET
        else:
            releases_url = self.releases_url

        git_repository_url: None | str | Unset
        if isinstance(self.git_repository_url, Unset):
            git_repository_url = UNSET
        else:
            git_repository_url = self.git_repository_url

        tracked_app_version: None | str | Unset
        if isinstance(self.tracked_app_version, Unset):
            tracked_app_version = UNSET
        else:
            tracked_app_version = self.tracked_app_version

        latest_upstream_version: None | str | Unset
        if isinstance(self.latest_upstream_version, Unset):
            latest_upstream_version = UNSET
        else:
            latest_upstream_version = self.latest_upstream_version

        upstream_checked_at: None | str | Unset
        if isinstance(self.upstream_checked_at, Unset):
            upstream_checked_at = UNSET
        elif isinstance(self.upstream_checked_at, datetime.datetime):
            upstream_checked_at = self.upstream_checked_at.isoformat()
        else:
            upstream_checked_at = self.upstream_checked_at

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
                "serial_number": serial_number,
                "upstream_outdated": upstream_outdated,
                "artifact_package": artifact_package,
                "dependency_count": dependency_count,
                "screenshot_url": screenshot_url,
                "price_monthly": price_monthly,
                "product_regular": product_regular,
                "product_ha": product_ha,
                "latest_block": latest_block,
            }
        )
        if claim is not UNSET:
            field_dict["claim"] = claim
        if short_description is not UNSET:
            field_dict["short_description"] = short_description
        if draft is not UNSET:
            field_dict["draft"] = draft
        if is_new is not UNSET:
            field_dict["is_new"] = is_new
        if supports_ha is not UNSET:
            field_dict["supports_ha"] = supports_ha
        if registry_url is not UNSET:
            field_dict["registry_url"] = registry_url
        if releases_url is not UNSET:
            field_dict["releases_url"] = releases_url
        if git_repository_url is not UNSET:
            field_dict["git_repository_url"] = git_repository_url
        if tracked_app_version is not UNSET:
            field_dict["tracked_app_version"] = tracked_app_version
        if latest_upstream_version is not UNSET:
            field_dict["latest_upstream_version"] = latest_upstream_version
        if upstream_checked_at is not UNSET:
            field_dict["upstream_checked_at"] = upstream_checked_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.artifact_package_catalogue import ArtifactPackageCatalogue
        from ..models.catalogue_app_list_active_condition_instances_item import (
            CatalogueAppListActiveConditionInstancesItem,
        )
        from ..models.catalogue_app_list_created import CatalogueAppListCreated
        from ..models.catalogue_app_list_latest_block_type_0 import CatalogueAppListLatestBlockType0
        from ..models.product_simple import ProductSimple

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
            active_condition_instances_item = CatalogueAppListActiveConditionInstancesItem.from_dict(
                active_condition_instances_item_data
            )

            active_condition_instances.append(active_condition_instances_item)

        def _parse_organization(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        organization = _parse_organization(d.pop("organization"))

        organization_priority = d.pop("organization_priority")

        def _parse_workspace(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        workspace = _parse_workspace(d.pop("workspace"))

        created = CatalogueAppListCreated.from_dict(d.pop("created"))

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

        serial_number = d.pop("serial_number")

        upstream_outdated = d.pop("upstream_outdated")

        artifact_package = ArtifactPackageCatalogue.from_dict(d.pop("artifact_package"))

        dependency_count = d.pop("dependency_count")

        screenshot_url = d.pop("screenshot_url")

        price_monthly = d.pop("price_monthly")

        product_regular = ProductSimple.from_dict(d.pop("product_regular"))

        product_ha = ProductSimple.from_dict(d.pop("product_ha"))

        def _parse_latest_block(data: object) -> CatalogueAppListLatestBlockType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latest_block_type_0 = CatalogueAppListLatestBlockType0.from_dict(data)

                return latest_block_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CatalogueAppListLatestBlockType0 | None, data)

        latest_block = _parse_latest_block(d.pop("latest_block"))

        claim = d.pop("claim", UNSET)

        def _parse_short_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        short_description = _parse_short_description(d.pop("short_description", UNSET))

        draft = d.pop("draft", UNSET)

        is_new = d.pop("is_new", UNSET)

        supports_ha = d.pop("supports_ha", UNSET)

        registry_url = d.pop("registry_url", UNSET)

        def _parse_releases_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        releases_url = _parse_releases_url(d.pop("releases_url", UNSET))

        def _parse_git_repository_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        git_repository_url = _parse_git_repository_url(d.pop("git_repository_url", UNSET))

        def _parse_tracked_app_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tracked_app_version = _parse_tracked_app_version(d.pop("tracked_app_version", UNSET))

        def _parse_latest_upstream_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_upstream_version = _parse_latest_upstream_version(d.pop("latest_upstream_version", UNSET))

        def _parse_upstream_checked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                upstream_checked_at_type_0 = datetime.datetime.fromisoformat(data)

                return upstream_checked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        upstream_checked_at = _parse_upstream_checked_at(d.pop("upstream_checked_at", UNSET))

        catalogue_app_list = cls(
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
            serial_number=serial_number,
            upstream_outdated=upstream_outdated,
            artifact_package=artifact_package,
            dependency_count=dependency_count,
            screenshot_url=screenshot_url,
            price_monthly=price_monthly,
            product_regular=product_regular,
            product_ha=product_ha,
            latest_block=latest_block,
            claim=claim,
            short_description=short_description,
            draft=draft,
            is_new=is_new,
            supports_ha=supports_ha,
            registry_url=registry_url,
            releases_url=releases_url,
            git_repository_url=git_repository_url,
            tracked_app_version=tracked_app_version,
            latest_upstream_version=latest_upstream_version,
            upstream_checked_at=upstream_checked_at,
        )

        catalogue_app_list.additional_properties = d
        return catalogue_app_list

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
