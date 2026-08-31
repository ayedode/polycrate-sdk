from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.created_by_component_enum import CreatedByComponentEnum, check_created_by_component_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.effective_criticality_enum import EffectiveCriticalityEnum, check_effective_criticality_enum
from ..models.generic_object_kind_enum import GenericObjectKindEnum, check_generic_object_kind_enum
from ..models.last_state_enum import LastStateEnum, check_last_state_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artifact_package_catalogue import ArtifactPackageCatalogue
    from ..models.catalogue_app_detail_created import CatalogueAppDetailCreated
    from ..models.catalogue_app_detail_deleted_by_user_type_0 import CatalogueAppDetailDeletedByUserType0
    from ..models.catalogue_app_detail_last_action_run_type_0 import CatalogueAppDetailLastActionRunType0
    from ..models.catalogue_app_detail_organization_type_0 import CatalogueAppDetailOrganizationType0
    from ..models.catalogue_app_detail_template_block_detail_type_0 import CatalogueAppDetailTemplateBlockDetailType0
    from ..models.catalogue_app_detail_workspace_type_0 import CatalogueAppDetailWorkspaceType0
    from ..models.catalogue_app_simple import CatalogueAppSimple
    from ..models.product_simple import ProductSimple


T = TypeVar("T", bound="CatalogueAppDetail")


@_attrs_define
class CatalogueAppDetail:
    """Detail serializer for CatalogueApp with full data + validation.
    Handles Paradigma B (API-based Create/Edit) per .specs/0.12.0/catalogue-app.md

        Attributes:
            id (UUID):
            created (CatalogueAppDetailCreated):
            organization (CatalogueAppDetailOrganizationType0 | None):
            workspace (CatalogueAppDetailWorkspaceType0 | None):
            url (str): Gibt die absolute URL zum Object zurück.
            icon_url (str): Gibt die Icon-URL des Objects zurück (für Dashboard Component Header).
                Fällt auf class_icon_url zurück wenn get_icon_url() leer ist.
            is_class_icon (bool):
            effective_slo_target (float | None):
            effective_sla_target (float | None):
            effective_criticality (EffectiveCriticalityEnum | None):
            last_action_run (CatalogueAppDetailLastActionRunType0 | None):
            deleted_by_user (CatalogueAppDetailDeletedByUserType0 | None):
            artifact_package_detail (ArtifactPackageCatalogue): Rich ArtifactPackage serializer for CatalogueApp / catalogue
                context.

                Uses ``ArtifactDerivedFieldsMixin`` to transparently expose metadata
                (version, license, changelog, readme …) from the latest Artifact of
                the package - or from a specifically requested one when
                ``_artifact_override`` is set in the serializer context.

                Per .specs/0.12.0/catalogue-app.md
            dependencies_detail (list[CatalogueAppSimple]):
            screenshot_url (str):
            template_block_detail (CatalogueAppDetailTemplateBlockDetailType0 | None):
            product_regular (ProductSimple): Compact serializer for embedding Product as FK reference.
            product_ha (ProductSimple): Compact serializer for embedding Product as FK reference.
            upstream_outdated (bool):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            deleted_at (datetime.datetime | None): Timestamp when this object was soft-deleted. Null if not deleted.
            is_deleted (bool): True when this object has been soft-deleted. The object remains in the database while cleanup
                runs. Poll this field after DELETE 202; the object disappears (404) once cleanup is complete.
            state (LastStateEnum): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            state_reason (None | str):
            last_state (LastStateEnum): * `OK` - Ok
                * `WARNING` - Warning
                * `CRITICAL` - Critical
                * `READY` - Ready
                * `DEGRADED` - Degraded
                * `DOWN` - Down
            last_state_change (datetime.datetime | None):
            reconciliation_running (bool):
            reconciliation_task_id (None | str):
            reconciliation_task_meta (Any): Task metadata for reconciliation progress tracking (e.g., step, progress,
                started_at)
            last_reconciliation (datetime.datetime | None):
            discovery_enabled (bool):
            discovery_running (bool):
            discovery_task_id (None | str):
            discovery_task_meta (Any): Task metadata for discovery progress tracking
            last_discovery (datetime.datetime | None):
            repair_running (bool):
            repair_task_id (None | str):
            repair_task_meta (Any): Task metadata for repair progress tracking
            last_repair (datetime.datetime | None):
            scope (ScopeEnum): * `system` - System
                * `user` - User
            conditions (Any): Conditions are managed by the API and will be added during the reconcile phase. Some
                conditions are `degrading`, meaning an object becomes DEGRADED if it has such a condition.
            actual_availability (str): Calculated actual availability as yearly average in %
            serial_number (int): Serial number from app catalogue (S/N)
            latest_upstream_version (None | str): Latest stable upstream version (denormalized from app-release notes).
            upstream_checked_at (datetime.datetime | None): Timestamp of the last upstream release sync.
            name (str | Unset): Object name
            display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
                from the name.
            labels (Any | Unset):
            annotations (Any | Unset):
            debug_mode (bool | Unset): Persists all Object Logs in the database
            provider (ProviderEnum | Unset): * `loopback` - Loopback
                * `hetzner_cloud` - HETZNER Cloud
                * `hetzner_robot` - HETZNER Robot
                * `bare_metal` - Bare-Metal
                * `powerdns` - PowerDNS
                * `cloudflare` - Cloudflare
                * `rook-ceph` - Rook Ceph
                * `polycrate` - Polycrate
                * `kubernetes` - Kubernetes
                * `helm` - Helm
                * `generic` - Generic
                * `victorialogs` - VictoriaLogs
                * `system` - System
            provider_reference (None | str | Unset):
            provider_id (None | str | Unset):
            reconciliation_enabled (bool | Unset):
            last_reconciliation_duration_seconds (float | None | Unset): Duration of the last reconciliation in seconds
            platform_service (bool | Unset):
            kind (GenericObjectKindEnum | Unset): * `generic` - Generic
            tolerations (Any | Unset): Tolerations match conditions. If a toleration for a condition exists for an object,
                the condition will not be applied.
            archived (bool | Unset): Archived objects are not shown in the UI and are not managed by the API.
            archived_at (datetime.datetime | None | Unset):
            archived_reason (None | str | Unset): The reason why the object was archived
            created_by_component (BlankEnum | CreatedByComponentEnum | None | Unset): Component that created this object:
                cli, operator, or api.

                * `cli` - CLI
                * `operator` - Operator
                * `api` - API
            target_availability (None | str | Unset): Target availability in % (overrides SystemConfig default). Null = use
                SystemConfig DEFAULT_TARGET_AVAILABILITY.
            slo_target (None | str | Unset): Internal SLO target in %. Null = use SystemConfig DEFAULT_SLO_TARGET
            slo_window_days (int | None | Unset): SLO window in days. Null = use SystemConfig DEFAULT_SLO_WINDOW_DAYS
            slo_availability (str | Unset): Calculated SLO availability in % (updated in reconcile)
            sla_target (None | str | Unset): Contractual SLA target in %. Null = use SystemConfig DEFAULT_SLA_TARGET
            sla_window_days (int | None | Unset): SLA window in days. Null = use SystemConfig DEFAULT_SLA_WINDOW_DAYS (365)
            sla_availability (str | Unset): Calculated SLA availability in % (updated in reconcile)
            criticality (BlankEnum | CriticalityEnum | None | Unset): Criticality level. Null = inherit from workspace, then
                org. Explicit value overrides inheritance.

                * `high` - High
                * `medium` - Medium
                * `low` - Low
            managed_by_object_id (None | str | Unset):
            platform_dns_record_created (bool | Unset):
            short_description (None | str | Unset): What is this app? (mapped from Baserow 'what_is')
            claim (str | Unset): Short marketing claim (mapped from Baserow 'info')
            draft (bool | Unset): Draft apps are not visible in the public catalogue
            is_new (bool | Unset): Highlight as new app in the catalogue
            screenshot (None | str | Unset): App screenshot (stored in S3)
            markdown_content (None | str | Unset): Detailed app description in Markdown
            supports_ha (bool | Unset): Whether HA (zero-downtime) deployment mode is supported for this app. Mirrors
                block.SupportsHA (CLI YAML: supports_ha).
            ha_enabled_expression (None | str | Unset): Jinja2 boolean expression evaluated against block.config at
                reconciliation time. Returns True → HA product; False → regular product. Empty expression → ha_enabled=False
                (regular default). Example: block.config.cluster.replica_count > 2
            registry_url (str | Unset): OCI registry URL for this app (e.g. cargo.ayedo.cloud/ayedo/k8s/n8n). Used to match
                template blocks by their content_url prefix.
            releases_url (None | str | Unset): GitHub releases page or API URL (preferred upstream source).
            git_repository_url (None | str | Unset): GitHub repository URL; releases derived when releases_url is empty.
            tracked_app_version (None | str | Unset): Packaged app version tracked by ayedo (from Hub/block sync or manual).
            archived_by (int | None | Unset): The user who archived the object
            managed_by_content_type (int | None | Unset):
            modified_by_user (int | None | Unset): The user who last modified the object
            created_by_user (int | None | Unset): The user who created the object
            artifact_package (None | Unset | UUID):
            dependencies (list[UUID] | Unset): Upstream dependencies (other CatalogueApps)
    """

    id: UUID
    created: CatalogueAppDetailCreated
    organization: CatalogueAppDetailOrganizationType0 | None
    workspace: CatalogueAppDetailWorkspaceType0 | None
    url: str
    icon_url: str
    is_class_icon: bool
    effective_slo_target: float | None
    effective_sla_target: float | None
    effective_criticality: EffectiveCriticalityEnum | None
    last_action_run: CatalogueAppDetailLastActionRunType0 | None
    deleted_by_user: CatalogueAppDetailDeletedByUserType0 | None
    artifact_package_detail: ArtifactPackageCatalogue
    dependencies_detail: list[CatalogueAppSimple]
    screenshot_url: str
    template_block_detail: CatalogueAppDetailTemplateBlockDetailType0 | None
    product_regular: ProductSimple
    product_ha: ProductSimple
    upstream_outdated: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime | None
    is_deleted: bool
    state: LastStateEnum
    state_reason: None | str
    last_state: LastStateEnum
    last_state_change: datetime.datetime | None
    reconciliation_running: bool
    reconciliation_task_id: None | str
    reconciliation_task_meta: Any
    last_reconciliation: datetime.datetime | None
    discovery_enabled: bool
    discovery_running: bool
    discovery_task_id: None | str
    discovery_task_meta: Any
    last_discovery: datetime.datetime | None
    repair_running: bool
    repair_task_id: None | str
    repair_task_meta: Any
    last_repair: datetime.datetime | None
    scope: ScopeEnum
    conditions: Any
    actual_availability: str
    serial_number: int
    latest_upstream_version: None | str
    upstream_checked_at: datetime.datetime | None
    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    last_reconciliation_duration_seconds: float | None | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: GenericObjectKindEnum | Unset = UNSET
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    created_by_component: BlankEnum | CreatedByComponentEnum | None | Unset = UNSET
    target_availability: None | str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_window_days: int | None | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_window_days: int | None | Unset = UNSET
    sla_availability: str | Unset = UNSET
    criticality: BlankEnum | CriticalityEnum | None | Unset = UNSET
    managed_by_object_id: None | str | Unset = UNSET
    platform_dns_record_created: bool | Unset = UNSET
    short_description: None | str | Unset = UNSET
    claim: str | Unset = UNSET
    draft: bool | Unset = UNSET
    is_new: bool | Unset = UNSET
    screenshot: None | str | Unset = UNSET
    markdown_content: None | str | Unset = UNSET
    supports_ha: bool | Unset = UNSET
    ha_enabled_expression: None | str | Unset = UNSET
    registry_url: str | Unset = UNSET
    releases_url: None | str | Unset = UNSET
    git_repository_url: None | str | Unset = UNSET
    tracked_app_version: None | str | Unset = UNSET
    archived_by: int | None | Unset = UNSET
    managed_by_content_type: int | None | Unset = UNSET
    modified_by_user: int | None | Unset = UNSET
    created_by_user: int | None | Unset = UNSET
    artifact_package: None | Unset | UUID = UNSET
    dependencies: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.catalogue_app_detail_deleted_by_user_type_0 import CatalogueAppDetailDeletedByUserType0
        from ..models.catalogue_app_detail_last_action_run_type_0 import CatalogueAppDetailLastActionRunType0
        from ..models.catalogue_app_detail_organization_type_0 import CatalogueAppDetailOrganizationType0
        from ..models.catalogue_app_detail_template_block_detail_type_0 import (
            CatalogueAppDetailTemplateBlockDetailType0,
        )
        from ..models.catalogue_app_detail_workspace_type_0 import CatalogueAppDetailWorkspaceType0

        id = str(self.id)

        created = self.created.to_dict()

        organization: dict[str, Any] | None
        if isinstance(self.organization, CatalogueAppDetailOrganizationType0):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        workspace: dict[str, Any] | None
        if isinstance(self.workspace, CatalogueAppDetailWorkspaceType0):
            workspace = self.workspace.to_dict()
        else:
            workspace = self.workspace

        url = self.url

        icon_url = self.icon_url

        is_class_icon = self.is_class_icon

        effective_slo_target: float | None
        effective_slo_target = self.effective_slo_target

        effective_sla_target: float | None
        effective_sla_target = self.effective_sla_target

        effective_criticality: None | str
        if isinstance(self.effective_criticality, str):
            effective_criticality = self.effective_criticality
        else:
            effective_criticality = self.effective_criticality

        last_action_run: dict[str, Any] | None
        if isinstance(self.last_action_run, CatalogueAppDetailLastActionRunType0):
            last_action_run = self.last_action_run.to_dict()
        else:
            last_action_run = self.last_action_run

        deleted_by_user: dict[str, Any] | None
        if isinstance(self.deleted_by_user, CatalogueAppDetailDeletedByUserType0):
            deleted_by_user = self.deleted_by_user.to_dict()
        else:
            deleted_by_user = self.deleted_by_user

        artifact_package_detail = self.artifact_package_detail.to_dict()

        dependencies_detail = []
        for dependencies_detail_item_data in self.dependencies_detail:
            dependencies_detail_item = dependencies_detail_item_data.to_dict()
            dependencies_detail.append(dependencies_detail_item)

        screenshot_url = self.screenshot_url

        template_block_detail: dict[str, Any] | None
        if isinstance(self.template_block_detail, CatalogueAppDetailTemplateBlockDetailType0):
            template_block_detail = self.template_block_detail.to_dict()
        else:
            template_block_detail = self.template_block_detail

        product_regular = self.product_regular.to_dict()

        product_ha = self.product_ha.to_dict()

        upstream_outdated = self.upstream_outdated

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        is_deleted = self.is_deleted

        state: str = self.state

        state_reason: None | str
        state_reason = self.state_reason

        last_state: str = self.last_state

        last_state_change: None | str
        if isinstance(self.last_state_change, datetime.datetime):
            last_state_change = self.last_state_change.isoformat()
        else:
            last_state_change = self.last_state_change

        reconciliation_running = self.reconciliation_running

        reconciliation_task_id: None | str
        reconciliation_task_id = self.reconciliation_task_id

        reconciliation_task_meta = self.reconciliation_task_meta

        last_reconciliation: None | str
        if isinstance(self.last_reconciliation, datetime.datetime):
            last_reconciliation = self.last_reconciliation.isoformat()
        else:
            last_reconciliation = self.last_reconciliation

        discovery_enabled = self.discovery_enabled

        discovery_running = self.discovery_running

        discovery_task_id: None | str
        discovery_task_id = self.discovery_task_id

        discovery_task_meta = self.discovery_task_meta

        last_discovery: None | str
        if isinstance(self.last_discovery, datetime.datetime):
            last_discovery = self.last_discovery.isoformat()
        else:
            last_discovery = self.last_discovery

        repair_running = self.repair_running

        repair_task_id: None | str
        repair_task_id = self.repair_task_id

        repair_task_meta = self.repair_task_meta

        last_repair: None | str
        if isinstance(self.last_repair, datetime.datetime):
            last_repair = self.last_repair.isoformat()
        else:
            last_repair = self.last_repair

        scope: str = self.scope

        conditions = self.conditions

        actual_availability = self.actual_availability

        serial_number = self.serial_number

        latest_upstream_version: None | str
        latest_upstream_version = self.latest_upstream_version

        upstream_checked_at: None | str
        if isinstance(self.upstream_checked_at, datetime.datetime):
            upstream_checked_at = self.upstream_checked_at.isoformat()
        else:
            upstream_checked_at = self.upstream_checked_at

        name = self.name

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        labels = self.labels

        annotations = self.annotations

        debug_mode = self.debug_mode

        provider: str | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        provider_reference: None | str | Unset
        if isinstance(self.provider_reference, Unset):
            provider_reference = UNSET
        else:
            provider_reference = self.provider_reference

        provider_id: None | str | Unset
        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = self.provider_id

        reconciliation_enabled = self.reconciliation_enabled

        last_reconciliation_duration_seconds: float | None | Unset
        if isinstance(self.last_reconciliation_duration_seconds, Unset):
            last_reconciliation_duration_seconds = UNSET
        else:
            last_reconciliation_duration_seconds = self.last_reconciliation_duration_seconds

        platform_service = self.platform_service

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        tolerations = self.tolerations

        archived = self.archived

        archived_at: None | str | Unset
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        archived_reason: None | str | Unset
        if isinstance(self.archived_reason, Unset):
            archived_reason = UNSET
        else:
            archived_reason = self.archived_reason

        created_by_component: None | str | Unset
        if isinstance(self.created_by_component, Unset):
            created_by_component = UNSET
        elif isinstance(self.created_by_component, str):
            created_by_component = self.created_by_component
        elif isinstance(self.created_by_component, str):
            created_by_component = self.created_by_component
        else:
            created_by_component = self.created_by_component

        target_availability: None | str | Unset
        if isinstance(self.target_availability, Unset):
            target_availability = UNSET
        else:
            target_availability = self.target_availability

        slo_target: None | str | Unset
        if isinstance(self.slo_target, Unset):
            slo_target = UNSET
        else:
            slo_target = self.slo_target

        slo_window_days: int | None | Unset
        if isinstance(self.slo_window_days, Unset):
            slo_window_days = UNSET
        else:
            slo_window_days = self.slo_window_days

        slo_availability = self.slo_availability

        sla_target: None | str | Unset
        if isinstance(self.sla_target, Unset):
            sla_target = UNSET
        else:
            sla_target = self.sla_target

        sla_window_days: int | None | Unset
        if isinstance(self.sla_window_days, Unset):
            sla_window_days = UNSET
        else:
            sla_window_days = self.sla_window_days

        sla_availability = self.sla_availability

        criticality: None | str | Unset
        if isinstance(self.criticality, Unset):
            criticality = UNSET
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        else:
            criticality = self.criticality

        managed_by_object_id: None | str | Unset
        if isinstance(self.managed_by_object_id, Unset):
            managed_by_object_id = UNSET
        else:
            managed_by_object_id = self.managed_by_object_id

        platform_dns_record_created = self.platform_dns_record_created

        short_description: None | str | Unset
        if isinstance(self.short_description, Unset):
            short_description = UNSET
        else:
            short_description = self.short_description

        claim = self.claim

        draft = self.draft

        is_new = self.is_new

        screenshot: None | str | Unset
        if isinstance(self.screenshot, Unset):
            screenshot = UNSET
        else:
            screenshot = self.screenshot

        markdown_content: None | str | Unset
        if isinstance(self.markdown_content, Unset):
            markdown_content = UNSET
        else:
            markdown_content = self.markdown_content

        supports_ha = self.supports_ha

        ha_enabled_expression: None | str | Unset
        if isinstance(self.ha_enabled_expression, Unset):
            ha_enabled_expression = UNSET
        else:
            ha_enabled_expression = self.ha_enabled_expression

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

        archived_by: int | None | Unset
        if isinstance(self.archived_by, Unset):
            archived_by = UNSET
        else:
            archived_by = self.archived_by

        managed_by_content_type: int | None | Unset
        if isinstance(self.managed_by_content_type, Unset):
            managed_by_content_type = UNSET
        else:
            managed_by_content_type = self.managed_by_content_type

        modified_by_user: int | None | Unset
        if isinstance(self.modified_by_user, Unset):
            modified_by_user = UNSET
        else:
            modified_by_user = self.modified_by_user

        created_by_user: int | None | Unset
        if isinstance(self.created_by_user, Unset):
            created_by_user = UNSET
        else:
            created_by_user = self.created_by_user

        artifact_package: None | str | Unset
        if isinstance(self.artifact_package, Unset):
            artifact_package = UNSET
        elif isinstance(self.artifact_package, UUID):
            artifact_package = str(self.artifact_package)
        else:
            artifact_package = self.artifact_package

        dependencies: list[str] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = []
            for dependencies_item_data in self.dependencies:
                dependencies_item = str(dependencies_item_data)
                dependencies.append(dependencies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created": created,
                "organization": organization,
                "workspace": workspace,
                "url": url,
                "icon_url": icon_url,
                "is_class_icon": is_class_icon,
                "effective_slo_target": effective_slo_target,
                "effective_sla_target": effective_sla_target,
                "effective_criticality": effective_criticality,
                "last_action_run": last_action_run,
                "deleted_by_user": deleted_by_user,
                "artifact_package_detail": artifact_package_detail,
                "dependencies_detail": dependencies_detail,
                "screenshot_url": screenshot_url,
                "template_block_detail": template_block_detail,
                "product_regular": product_regular,
                "product_ha": product_ha,
                "upstream_outdated": upstream_outdated,
                "created_at": created_at,
                "updated_at": updated_at,
                "deleted_at": deleted_at,
                "is_deleted": is_deleted,
                "state": state,
                "state_reason": state_reason,
                "last_state": last_state,
                "last_state_change": last_state_change,
                "reconciliation_running": reconciliation_running,
                "reconciliation_task_id": reconciliation_task_id,
                "reconciliation_task_meta": reconciliation_task_meta,
                "last_reconciliation": last_reconciliation,
                "discovery_enabled": discovery_enabled,
                "discovery_running": discovery_running,
                "discovery_task_id": discovery_task_id,
                "discovery_task_meta": discovery_task_meta,
                "last_discovery": last_discovery,
                "repair_running": repair_running,
                "repair_task_id": repair_task_id,
                "repair_task_meta": repair_task_meta,
                "last_repair": last_repair,
                "scope": scope,
                "conditions": conditions,
                "actual_availability": actual_availability,
                "serial_number": serial_number,
                "latest_upstream_version": latest_upstream_version,
                "upstream_checked_at": upstream_checked_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if labels is not UNSET:
            field_dict["labels"] = labels
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if debug_mode is not UNSET:
            field_dict["debug_mode"] = debug_mode
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_reference is not UNSET:
            field_dict["provider_reference"] = provider_reference
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if reconciliation_enabled is not UNSET:
            field_dict["reconciliation_enabled"] = reconciliation_enabled
        if last_reconciliation_duration_seconds is not UNSET:
            field_dict["last_reconciliation_duration_seconds"] = last_reconciliation_duration_seconds
        if platform_service is not UNSET:
            field_dict["platform_service"] = platform_service
        if kind is not UNSET:
            field_dict["kind"] = kind
        if tolerations is not UNSET:
            field_dict["tolerations"] = tolerations
        if archived is not UNSET:
            field_dict["archived"] = archived
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if archived_reason is not UNSET:
            field_dict["archived_reason"] = archived_reason
        if created_by_component is not UNSET:
            field_dict["created_by_component"] = created_by_component
        if target_availability is not UNSET:
            field_dict["target_availability"] = target_availability
        if slo_target is not UNSET:
            field_dict["slo_target"] = slo_target
        if slo_window_days is not UNSET:
            field_dict["slo_window_days"] = slo_window_days
        if slo_availability is not UNSET:
            field_dict["slo_availability"] = slo_availability
        if sla_target is not UNSET:
            field_dict["sla_target"] = sla_target
        if sla_window_days is not UNSET:
            field_dict["sla_window_days"] = sla_window_days
        if sla_availability is not UNSET:
            field_dict["sla_availability"] = sla_availability
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if managed_by_object_id is not UNSET:
            field_dict["managed_by_object_id"] = managed_by_object_id
        if platform_dns_record_created is not UNSET:
            field_dict["platform_dns_record_created"] = platform_dns_record_created
        if short_description is not UNSET:
            field_dict["short_description"] = short_description
        if claim is not UNSET:
            field_dict["claim"] = claim
        if draft is not UNSET:
            field_dict["draft"] = draft
        if is_new is not UNSET:
            field_dict["is_new"] = is_new
        if screenshot is not UNSET:
            field_dict["screenshot"] = screenshot
        if markdown_content is not UNSET:
            field_dict["markdown_content"] = markdown_content
        if supports_ha is not UNSET:
            field_dict["supports_ha"] = supports_ha
        if ha_enabled_expression is not UNSET:
            field_dict["ha_enabled_expression"] = ha_enabled_expression
        if registry_url is not UNSET:
            field_dict["registry_url"] = registry_url
        if releases_url is not UNSET:
            field_dict["releases_url"] = releases_url
        if git_repository_url is not UNSET:
            field_dict["git_repository_url"] = git_repository_url
        if tracked_app_version is not UNSET:
            field_dict["tracked_app_version"] = tracked_app_version
        if archived_by is not UNSET:
            field_dict["archived_by"] = archived_by
        if managed_by_content_type is not UNSET:
            field_dict["managed_by_content_type"] = managed_by_content_type
        if modified_by_user is not UNSET:
            field_dict["modified_by_user"] = modified_by_user
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if artifact_package is not UNSET:
            field_dict["artifact_package"] = artifact_package
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.artifact_package_catalogue import ArtifactPackageCatalogue
        from ..models.catalogue_app_detail_created import CatalogueAppDetailCreated
        from ..models.catalogue_app_detail_deleted_by_user_type_0 import CatalogueAppDetailDeletedByUserType0
        from ..models.catalogue_app_detail_last_action_run_type_0 import CatalogueAppDetailLastActionRunType0
        from ..models.catalogue_app_detail_organization_type_0 import CatalogueAppDetailOrganizationType0
        from ..models.catalogue_app_detail_template_block_detail_type_0 import (
            CatalogueAppDetailTemplateBlockDetailType0,
        )
        from ..models.catalogue_app_detail_workspace_type_0 import CatalogueAppDetailWorkspaceType0
        from ..models.catalogue_app_simple import CatalogueAppSimple
        from ..models.product_simple import ProductSimple

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        created = CatalogueAppDetailCreated.from_dict(d.pop("created"))

        def _parse_organization(data: object) -> CatalogueAppDetailOrganizationType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = CatalogueAppDetailOrganizationType0.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CatalogueAppDetailOrganizationType0 | None, data)

        organization = _parse_organization(d.pop("organization"))

        def _parse_workspace(data: object) -> CatalogueAppDetailWorkspaceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                workspace_type_0 = CatalogueAppDetailWorkspaceType0.from_dict(data)

                return workspace_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CatalogueAppDetailWorkspaceType0 | None, data)

        workspace = _parse_workspace(d.pop("workspace"))

        url = d.pop("url")

        icon_url = d.pop("icon_url")

        is_class_icon = d.pop("is_class_icon")

        def _parse_effective_slo_target(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        effective_slo_target = _parse_effective_slo_target(d.pop("effective_slo_target"))

        def _parse_effective_sla_target(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        effective_sla_target = _parse_effective_sla_target(d.pop("effective_sla_target"))

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

        def _parse_last_action_run(data: object) -> CatalogueAppDetailLastActionRunType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                last_action_run_type_0 = CatalogueAppDetailLastActionRunType0.from_dict(data)

                return last_action_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CatalogueAppDetailLastActionRunType0 | None, data)

        last_action_run = _parse_last_action_run(d.pop("last_action_run"))

        def _parse_deleted_by_user(data: object) -> CatalogueAppDetailDeletedByUserType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_user_type_0 = CatalogueAppDetailDeletedByUserType0.from_dict(data)

                return deleted_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CatalogueAppDetailDeletedByUserType0 | None, data)

        deleted_by_user = _parse_deleted_by_user(d.pop("deleted_by_user"))

        artifact_package_detail = ArtifactPackageCatalogue.from_dict(d.pop("artifact_package_detail"))

        dependencies_detail = []
        _dependencies_detail = d.pop("dependencies_detail")
        for dependencies_detail_item_data in _dependencies_detail:
            dependencies_detail_item = CatalogueAppSimple.from_dict(dependencies_detail_item_data)

            dependencies_detail.append(dependencies_detail_item)

        screenshot_url = d.pop("screenshot_url")

        def _parse_template_block_detail(data: object) -> CatalogueAppDetailTemplateBlockDetailType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                template_block_detail_type_0 = CatalogueAppDetailTemplateBlockDetailType0.from_dict(data)

                return template_block_detail_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CatalogueAppDetailTemplateBlockDetailType0 | None, data)

        template_block_detail = _parse_template_block_detail(d.pop("template_block_detail"))

        product_regular = ProductSimple.from_dict(d.pop("product_regular"))

        product_ha = ProductSimple.from_dict(d.pop("product_ha"))

        upstream_outdated = d.pop("upstream_outdated")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_deleted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at"))

        is_deleted = d.pop("is_deleted")

        state = check_last_state_enum(d.pop("state"))

        def _parse_state_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state_reason = _parse_state_reason(d.pop("state_reason"))

        last_state = check_last_state_enum(d.pop("last_state"))

        def _parse_last_state_change(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_state_change_type_0 = datetime.datetime.fromisoformat(data)

                return last_state_change_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_state_change = _parse_last_state_change(d.pop("last_state_change"))

        reconciliation_running = d.pop("reconciliation_running")

        def _parse_reconciliation_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reconciliation_task_id = _parse_reconciliation_task_id(d.pop("reconciliation_task_id"))

        reconciliation_task_meta = d.pop("reconciliation_task_meta")

        def _parse_last_reconciliation(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_reconciliation_type_0 = datetime.datetime.fromisoformat(data)

                return last_reconciliation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_reconciliation = _parse_last_reconciliation(d.pop("last_reconciliation"))

        discovery_enabled = d.pop("discovery_enabled")

        discovery_running = d.pop("discovery_running")

        def _parse_discovery_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        discovery_task_id = _parse_discovery_task_id(d.pop("discovery_task_id"))

        discovery_task_meta = d.pop("discovery_task_meta")

        def _parse_last_discovery(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_discovery_type_0 = datetime.datetime.fromisoformat(data)

                return last_discovery_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_discovery = _parse_last_discovery(d.pop("last_discovery"))

        repair_running = d.pop("repair_running")

        def _parse_repair_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        repair_task_id = _parse_repair_task_id(d.pop("repair_task_id"))

        repair_task_meta = d.pop("repair_task_meta")

        def _parse_last_repair(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_repair_type_0 = datetime.datetime.fromisoformat(data)

                return last_repair_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_repair = _parse_last_repair(d.pop("last_repair"))

        scope = check_scope_enum(d.pop("scope"))

        conditions = d.pop("conditions")

        actual_availability = d.pop("actual_availability")

        serial_number = d.pop("serial_number")

        def _parse_latest_upstream_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        latest_upstream_version = _parse_latest_upstream_version(d.pop("latest_upstream_version"))

        def _parse_upstream_checked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                upstream_checked_at_type_0 = datetime.datetime.fromisoformat(data)

                return upstream_checked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        upstream_checked_at = _parse_upstream_checked_at(d.pop("upstream_checked_at"))

        name = d.pop("name", UNSET)

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        labels = d.pop("labels", UNSET)

        annotations = d.pop("annotations", UNSET)

        debug_mode = d.pop("debug_mode", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: ProviderEnum | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_provider_enum(_provider)

        def _parse_provider_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_reference = _parse_provider_reference(d.pop("provider_reference", UNSET))

        def _parse_provider_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        provider_id = _parse_provider_id(d.pop("provider_id", UNSET))

        reconciliation_enabled = d.pop("reconciliation_enabled", UNSET)

        def _parse_last_reconciliation_duration_seconds(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        last_reconciliation_duration_seconds = _parse_last_reconciliation_duration_seconds(
            d.pop("last_reconciliation_duration_seconds", UNSET)
        )

        platform_service = d.pop("platform_service", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: GenericObjectKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_generic_object_kind_enum(_kind)

        tolerations = d.pop("tolerations", UNSET)

        archived = d.pop("archived", UNSET)

        def _parse_archived_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = datetime.datetime.fromisoformat(data)

                return archived_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        archived_at = _parse_archived_at(d.pop("archived_at", UNSET))

        def _parse_archived_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        archived_reason = _parse_archived_reason(d.pop("archived_reason", UNSET))

        def _parse_created_by_component(data: object) -> BlankEnum | CreatedByComponentEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_component_type_0 = check_created_by_component_enum(data)

                return created_by_component_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_component_type_1 = check_blank_enum(data)

                return created_by_component_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | CreatedByComponentEnum | None | Unset, data)

        created_by_component = _parse_created_by_component(d.pop("created_by_component", UNSET))

        def _parse_target_availability(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_availability = _parse_target_availability(d.pop("target_availability", UNSET))

        def _parse_slo_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slo_target = _parse_slo_target(d.pop("slo_target", UNSET))

        def _parse_slo_window_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        slo_window_days = _parse_slo_window_days(d.pop("slo_window_days", UNSET))

        slo_availability = d.pop("slo_availability", UNSET)

        def _parse_sla_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sla_target = _parse_sla_target(d.pop("sla_target", UNSET))

        def _parse_sla_window_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sla_window_days = _parse_sla_window_days(d.pop("sla_window_days", UNSET))

        sla_availability = d.pop("sla_availability", UNSET)

        def _parse_criticality(data: object) -> BlankEnum | CriticalityEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_0 = check_criticality_enum(data)

                return criticality_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_1 = check_blank_enum(data)

                return criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(BlankEnum | CriticalityEnum | None | Unset, data)

        criticality = _parse_criticality(d.pop("criticality", UNSET))

        def _parse_managed_by_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        managed_by_object_id = _parse_managed_by_object_id(d.pop("managed_by_object_id", UNSET))

        platform_dns_record_created = d.pop("platform_dns_record_created", UNSET)

        def _parse_short_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        short_description = _parse_short_description(d.pop("short_description", UNSET))

        claim = d.pop("claim", UNSET)

        draft = d.pop("draft", UNSET)

        is_new = d.pop("is_new", UNSET)

        def _parse_screenshot(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        screenshot = _parse_screenshot(d.pop("screenshot", UNSET))

        def _parse_markdown_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        markdown_content = _parse_markdown_content(d.pop("markdown_content", UNSET))

        supports_ha = d.pop("supports_ha", UNSET)

        def _parse_ha_enabled_expression(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ha_enabled_expression = _parse_ha_enabled_expression(d.pop("ha_enabled_expression", UNSET))

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

        def _parse_archived_by(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        archived_by = _parse_archived_by(d.pop("archived_by", UNSET))

        def _parse_managed_by_content_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        managed_by_content_type = _parse_managed_by_content_type(d.pop("managed_by_content_type", UNSET))

        def _parse_modified_by_user(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        modified_by_user = _parse_modified_by_user(d.pop("modified_by_user", UNSET))

        def _parse_created_by_user(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        created_by_user = _parse_created_by_user(d.pop("created_by_user", UNSET))

        def _parse_artifact_package(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                artifact_package_type_0 = UUID(data)

                return artifact_package_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        artifact_package = _parse_artifact_package(d.pop("artifact_package", UNSET))

        _dependencies = d.pop("dependencies", UNSET)
        dependencies: list[UUID] | Unset = UNSET
        if _dependencies is not UNSET:
            dependencies = []
            for dependencies_item_data in _dependencies:
                dependencies_item = UUID(dependencies_item_data)

                dependencies.append(dependencies_item)

        catalogue_app_detail = cls(
            id=id,
            created=created,
            organization=organization,
            workspace=workspace,
            url=url,
            icon_url=icon_url,
            is_class_icon=is_class_icon,
            effective_slo_target=effective_slo_target,
            effective_sla_target=effective_sla_target,
            effective_criticality=effective_criticality,
            last_action_run=last_action_run,
            deleted_by_user=deleted_by_user,
            artifact_package_detail=artifact_package_detail,
            dependencies_detail=dependencies_detail,
            screenshot_url=screenshot_url,
            template_block_detail=template_block_detail,
            product_regular=product_regular,
            product_ha=product_ha,
            upstream_outdated=upstream_outdated,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
            is_deleted=is_deleted,
            state=state,
            state_reason=state_reason,
            last_state=last_state,
            last_state_change=last_state_change,
            reconciliation_running=reconciliation_running,
            reconciliation_task_id=reconciliation_task_id,
            reconciliation_task_meta=reconciliation_task_meta,
            last_reconciliation=last_reconciliation,
            discovery_enabled=discovery_enabled,
            discovery_running=discovery_running,
            discovery_task_id=discovery_task_id,
            discovery_task_meta=discovery_task_meta,
            last_discovery=last_discovery,
            repair_running=repair_running,
            repair_task_id=repair_task_id,
            repair_task_meta=repair_task_meta,
            last_repair=last_repair,
            scope=scope,
            conditions=conditions,
            actual_availability=actual_availability,
            serial_number=serial_number,
            latest_upstream_version=latest_upstream_version,
            upstream_checked_at=upstream_checked_at,
            name=name,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            debug_mode=debug_mode,
            provider=provider,
            provider_reference=provider_reference,
            provider_id=provider_id,
            reconciliation_enabled=reconciliation_enabled,
            last_reconciliation_duration_seconds=last_reconciliation_duration_seconds,
            platform_service=platform_service,
            kind=kind,
            tolerations=tolerations,
            archived=archived,
            archived_at=archived_at,
            archived_reason=archived_reason,
            created_by_component=created_by_component,
            target_availability=target_availability,
            slo_target=slo_target,
            slo_window_days=slo_window_days,
            slo_availability=slo_availability,
            sla_target=sla_target,
            sla_window_days=sla_window_days,
            sla_availability=sla_availability,
            criticality=criticality,
            managed_by_object_id=managed_by_object_id,
            platform_dns_record_created=platform_dns_record_created,
            short_description=short_description,
            claim=claim,
            draft=draft,
            is_new=is_new,
            screenshot=screenshot,
            markdown_content=markdown_content,
            supports_ha=supports_ha,
            ha_enabled_expression=ha_enabled_expression,
            registry_url=registry_url,
            releases_url=releases_url,
            git_repository_url=git_repository_url,
            tracked_app_version=tracked_app_version,
            archived_by=archived_by,
            managed_by_content_type=managed_by_content_type,
            modified_by_user=modified_by_user,
            created_by_user=created_by_user,
            artifact_package=artifact_package,
            dependencies=dependencies,
        )

        catalogue_app_detail.additional_properties = d
        return catalogue_app_detail

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
