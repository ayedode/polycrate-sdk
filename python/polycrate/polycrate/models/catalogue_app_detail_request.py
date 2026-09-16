from __future__ import annotations

import datetime
from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.created_by_component_enum import CreatedByComponentEnum, check_created_by_component_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.generic_object_kind_enum import GenericObjectKindEnum, check_generic_object_kind_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="CatalogueAppDetailRequest")


@_attrs_define
class CatalogueAppDetailRequest:
    """Detail serializer for CatalogueApp with full data + validation.
    Handles Paradigma B (API-based Create/Edit) per .specs/0.12.0/catalogue-app.md

        Attributes:
            serial_number (int): Serial number from app catalogue (S/N)
            name (str | Unset): Object name
            product_regular_id (None | Unset | UUID):
            product_ha_id (None | Unset | UUID):
            maintainer_id (int | None | Unset):
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
            screenshot (File | None | Unset): App screenshot (stored in S3)
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

    serial_number: int
    name: str | Unset = UNSET
    product_regular_id: None | Unset | UUID = UNSET
    product_ha_id: None | Unset | UUID = UNSET
    maintainer_id: int | None | Unset = UNSET
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
    screenshot: File | None | Unset = UNSET
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
        serial_number = self.serial_number

        name = self.name

        product_regular_id: None | str | Unset
        if isinstance(self.product_regular_id, Unset):
            product_regular_id = UNSET
        elif isinstance(self.product_regular_id, UUID):
            product_regular_id = str(self.product_regular_id)
        else:
            product_regular_id = self.product_regular_id

        product_ha_id: None | str | Unset
        if isinstance(self.product_ha_id, Unset):
            product_ha_id = UNSET
        elif isinstance(self.product_ha_id, UUID):
            product_ha_id = str(self.product_ha_id)
        else:
            product_ha_id = self.product_ha_id

        maintainer_id: int | None | Unset
        if isinstance(self.maintainer_id, Unset):
            maintainer_id = UNSET
        else:
            maintainer_id = self.maintainer_id

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

        screenshot: FileTypes | None | Unset
        if isinstance(self.screenshot, Unset):
            screenshot = UNSET
        elif isinstance(self.screenshot, File):
            screenshot = self.screenshot.to_tuple()

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
                "serial_number": serial_number,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if product_regular_id is not UNSET:
            field_dict["product_regular_id"] = product_regular_id
        if product_ha_id is not UNSET:
            field_dict["product_ha_id"] = product_ha_id
        if maintainer_id is not UNSET:
            field_dict["maintainer_id"] = maintainer_id
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

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("serial_number", (None, str(self.serial_number).encode(), "text/plain")))

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.product_regular_id, Unset):
            if isinstance(self.product_regular_id, UUID):
                files.append(("product_regular_id", (None, str(self.product_regular_id), "text/plain")))
            else:
                files.append(("product_regular_id", (None, str(self.product_regular_id).encode(), "text/plain")))

        if not isinstance(self.product_ha_id, Unset):
            if isinstance(self.product_ha_id, UUID):
                files.append(("product_ha_id", (None, str(self.product_ha_id), "text/plain")))
            else:
                files.append(("product_ha_id", (None, str(self.product_ha_id).encode(), "text/plain")))

        if not isinstance(self.maintainer_id, Unset):
            if isinstance(self.maintainer_id, int):
                files.append(("maintainer_id", (None, str(self.maintainer_id).encode(), "text/plain")))
            else:
                files.append(("maintainer_id", (None, str(self.maintainer_id).encode(), "text/plain")))

        if not isinstance(self.display_name, Unset):
            if isinstance(self.display_name, str):
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))
            else:
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))

        if not isinstance(self.labels, Unset):
            files.append(("labels", (None, str(self.labels).encode(), "text/plain")))

        if not isinstance(self.annotations, Unset):
            files.append(("annotations", (None, str(self.annotations).encode(), "text/plain")))

        if not isinstance(self.debug_mode, Unset):
            files.append(("debug_mode", (None, str(self.debug_mode).encode(), "text/plain")))

        if not isinstance(self.provider, Unset):
            files.append(("provider", (None, str(self.provider).encode(), "text/plain")))

        if not isinstance(self.provider_reference, Unset):
            if isinstance(self.provider_reference, str):
                files.append(("provider_reference", (None, str(self.provider_reference).encode(), "text/plain")))
            else:
                files.append(("provider_reference", (None, str(self.provider_reference).encode(), "text/plain")))

        if not isinstance(self.provider_id, Unset):
            if isinstance(self.provider_id, str):
                files.append(("provider_id", (None, str(self.provider_id).encode(), "text/plain")))
            else:
                files.append(("provider_id", (None, str(self.provider_id).encode(), "text/plain")))

        if not isinstance(self.reconciliation_enabled, Unset):
            files.append(("reconciliation_enabled", (None, str(self.reconciliation_enabled).encode(), "text/plain")))

        if not isinstance(self.last_reconciliation_duration_seconds, Unset):
            if isinstance(self.last_reconciliation_duration_seconds, float):
                files.append(
                    (
                        "last_reconciliation_duration_seconds",
                        (None, str(self.last_reconciliation_duration_seconds).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "last_reconciliation_duration_seconds",
                        (None, str(self.last_reconciliation_duration_seconds).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.platform_service, Unset):
            files.append(("platform_service", (None, str(self.platform_service).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        if not isinstance(self.tolerations, Unset):
            files.append(("tolerations", (None, str(self.tolerations).encode(), "text/plain")))

        if not isinstance(self.archived, Unset):
            files.append(("archived", (None, str(self.archived).encode(), "text/plain")))

        if not isinstance(self.archived_at, Unset):
            if isinstance(self.archived_at, datetime.datetime):
                files.append(("archived_at", (None, self.archived_at.isoformat().encode(), "text/plain")))
            else:
                files.append(("archived_at", (None, str(self.archived_at).encode(), "text/plain")))

        if not isinstance(self.archived_reason, Unset):
            if isinstance(self.archived_reason, str):
                files.append(("archived_reason", (None, str(self.archived_reason).encode(), "text/plain")))
            else:
                files.append(("archived_reason", (None, str(self.archived_reason).encode(), "text/plain")))

        if not isinstance(self.created_by_component, Unset):
            if isinstance(self.created_by_component, str):
                files.append(("created_by_component", (None, str(self.created_by_component).encode(), "text/plain")))
            elif isinstance(self.created_by_component, str):
                files.append(("created_by_component", (None, str(self.created_by_component).encode(), "text/plain")))
            else:
                files.append(("created_by_component", (None, str(self.created_by_component).encode(), "text/plain")))

        if not isinstance(self.target_availability, Unset):
            if isinstance(self.target_availability, str):
                files.append(("target_availability", (None, str(self.target_availability).encode(), "text/plain")))
            else:
                files.append(("target_availability", (None, str(self.target_availability).encode(), "text/plain")))

        if not isinstance(self.slo_target, Unset):
            if isinstance(self.slo_target, str):
                files.append(("slo_target", (None, str(self.slo_target).encode(), "text/plain")))
            else:
                files.append(("slo_target", (None, str(self.slo_target).encode(), "text/plain")))

        if not isinstance(self.slo_window_days, Unset):
            if isinstance(self.slo_window_days, int):
                files.append(("slo_window_days", (None, str(self.slo_window_days).encode(), "text/plain")))
            else:
                files.append(("slo_window_days", (None, str(self.slo_window_days).encode(), "text/plain")))

        if not isinstance(self.slo_availability, Unset):
            files.append(("slo_availability", (None, str(self.slo_availability).encode(), "text/plain")))

        if not isinstance(self.sla_target, Unset):
            if isinstance(self.sla_target, str):
                files.append(("sla_target", (None, str(self.sla_target).encode(), "text/plain")))
            else:
                files.append(("sla_target", (None, str(self.sla_target).encode(), "text/plain")))

        if not isinstance(self.sla_window_days, Unset):
            if isinstance(self.sla_window_days, int):
                files.append(("sla_window_days", (None, str(self.sla_window_days).encode(), "text/plain")))
            else:
                files.append(("sla_window_days", (None, str(self.sla_window_days).encode(), "text/plain")))

        if not isinstance(self.sla_availability, Unset):
            files.append(("sla_availability", (None, str(self.sla_availability).encode(), "text/plain")))

        if not isinstance(self.criticality, Unset):
            if isinstance(self.criticality, str):
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))
            elif isinstance(self.criticality, str):
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))
            else:
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))

        if not isinstance(self.managed_by_object_id, Unset):
            if isinstance(self.managed_by_object_id, str):
                files.append(("managed_by_object_id", (None, str(self.managed_by_object_id).encode(), "text/plain")))
            else:
                files.append(("managed_by_object_id", (None, str(self.managed_by_object_id).encode(), "text/plain")))

        if not isinstance(self.platform_dns_record_created, Unset):
            files.append(
                ("platform_dns_record_created", (None, str(self.platform_dns_record_created).encode(), "text/plain"))
            )

        if not isinstance(self.short_description, Unset):
            if isinstance(self.short_description, str):
                files.append(("short_description", (None, str(self.short_description).encode(), "text/plain")))
            else:
                files.append(("short_description", (None, str(self.short_description).encode(), "text/plain")))

        if not isinstance(self.claim, Unset):
            files.append(("claim", (None, str(self.claim).encode(), "text/plain")))

        if not isinstance(self.draft, Unset):
            files.append(("draft", (None, str(self.draft).encode(), "text/plain")))

        if not isinstance(self.is_new, Unset):
            files.append(("is_new", (None, str(self.is_new).encode(), "text/plain")))

        if not isinstance(self.screenshot, Unset):
            if isinstance(self.screenshot, File):
                files.append(("screenshot", self.screenshot.to_tuple()))
            else:
                files.append(("screenshot", (None, str(self.screenshot).encode(), "text/plain")))

        if not isinstance(self.markdown_content, Unset):
            if isinstance(self.markdown_content, str):
                files.append(("markdown_content", (None, str(self.markdown_content).encode(), "text/plain")))
            else:
                files.append(("markdown_content", (None, str(self.markdown_content).encode(), "text/plain")))

        if not isinstance(self.supports_ha, Unset):
            files.append(("supports_ha", (None, str(self.supports_ha).encode(), "text/plain")))

        if not isinstance(self.ha_enabled_expression, Unset):
            if isinstance(self.ha_enabled_expression, str):
                files.append(("ha_enabled_expression", (None, str(self.ha_enabled_expression).encode(), "text/plain")))
            else:
                files.append(("ha_enabled_expression", (None, str(self.ha_enabled_expression).encode(), "text/plain")))

        if not isinstance(self.registry_url, Unset):
            files.append(("registry_url", (None, str(self.registry_url).encode(), "text/plain")))

        if not isinstance(self.releases_url, Unset):
            if isinstance(self.releases_url, str):
                files.append(("releases_url", (None, str(self.releases_url).encode(), "text/plain")))
            else:
                files.append(("releases_url", (None, str(self.releases_url).encode(), "text/plain")))

        if not isinstance(self.git_repository_url, Unset):
            if isinstance(self.git_repository_url, str):
                files.append(("git_repository_url", (None, str(self.git_repository_url).encode(), "text/plain")))
            else:
                files.append(("git_repository_url", (None, str(self.git_repository_url).encode(), "text/plain")))

        if not isinstance(self.tracked_app_version, Unset):
            if isinstance(self.tracked_app_version, str):
                files.append(("tracked_app_version", (None, str(self.tracked_app_version).encode(), "text/plain")))
            else:
                files.append(("tracked_app_version", (None, str(self.tracked_app_version).encode(), "text/plain")))

        if not isinstance(self.archived_by, Unset):
            if isinstance(self.archived_by, int):
                files.append(("archived_by", (None, str(self.archived_by).encode(), "text/plain")))
            else:
                files.append(("archived_by", (None, str(self.archived_by).encode(), "text/plain")))

        if not isinstance(self.managed_by_content_type, Unset):
            if isinstance(self.managed_by_content_type, int):
                files.append(
                    ("managed_by_content_type", (None, str(self.managed_by_content_type).encode(), "text/plain"))
                )
            else:
                files.append(
                    ("managed_by_content_type", (None, str(self.managed_by_content_type).encode(), "text/plain"))
                )

        if not isinstance(self.modified_by_user, Unset):
            if isinstance(self.modified_by_user, int):
                files.append(("modified_by_user", (None, str(self.modified_by_user).encode(), "text/plain")))
            else:
                files.append(("modified_by_user", (None, str(self.modified_by_user).encode(), "text/plain")))

        if not isinstance(self.created_by_user, Unset):
            if isinstance(self.created_by_user, int):
                files.append(("created_by_user", (None, str(self.created_by_user).encode(), "text/plain")))
            else:
                files.append(("created_by_user", (None, str(self.created_by_user).encode(), "text/plain")))

        if not isinstance(self.artifact_package, Unset):
            if isinstance(self.artifact_package, UUID):
                files.append(("artifact_package", (None, str(self.artifact_package), "text/plain")))
            else:
                files.append(("artifact_package", (None, str(self.artifact_package).encode(), "text/plain")))

        if not isinstance(self.dependencies, Unset):
            for dependencies_item_element in self.dependencies:
                files.append(("dependencies", (None, str(dependencies_item_element), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        serial_number = d.pop("serial_number")

        name = d.pop("name", UNSET)

        def _parse_product_regular_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                product_regular_id_type_0 = UUID(data)

                return product_regular_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        product_regular_id = _parse_product_regular_id(d.pop("product_regular_id", UNSET))

        def _parse_product_ha_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                product_ha_id_type_0 = UUID(data)

                return product_ha_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        product_ha_id = _parse_product_ha_id(d.pop("product_ha_id", UNSET))

        def _parse_maintainer_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        maintainer_id = _parse_maintainer_id(d.pop("maintainer_id", UNSET))

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

        def _parse_screenshot(data: object) -> File | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                screenshot_type_0 = File(payload=BytesIO(data))

                return screenshot_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(File | None | Unset, data)

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

        catalogue_app_detail_request = cls(
            serial_number=serial_number,
            name=name,
            product_regular_id=product_regular_id,
            product_ha_id=product_ha_id,
            maintainer_id=maintainer_id,
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

        catalogue_app_detail_request.additional_properties = d
        return catalogue_app_detail_request

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
