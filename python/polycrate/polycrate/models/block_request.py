from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.blank_enum import BlankEnum, check_blank_enum
from ..models.block_kind_enum import BlockKindEnum, check_block_kind_enum
from ..models.created_by_component_enum import CreatedByComponentEnum, check_created_by_component_enum
from ..models.criticality_enum import CriticalityEnum, check_criticality_enum
from ..models.provider_enum import ProviderEnum, check_provider_enum
from ..models.scope_enum import ScopeEnum, check_scope_enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="BlockRequest")


@_attrs_define
class BlockRequest:
    """Basis-Serializer für alle ManagedObject Detail-Endpoints.

    Enthält alle generischen Felder eines ManagedObjects.
    Subclasses erweitern diese Liste mit model-spezifischen Feldern.

    Inkludiert:
    - Alle BaseObject Felder (id, name, display_name, labels, annotations, timestamps)
    - Alle ManagedObject Felder (state, reconciliation, discovery, repair, conditions, etc.)
    - organization/workspace als generische ManagedObject-Referenzen (mit URL)
    - created: Kombifeld (created_at, created_at_humanized, created_by)
    - url: Absolute URL zum Object (via get_absolute_url())

    Usage:
        class K8sClusterDetailSerializer(ManagedObjectDetailSerializer):
            class Meta(ManagedObjectDetailSerializer.Meta):
                model = K8sCluster
                fields = ManagedObjectDetailSerializer.Meta.fields + ['kubeconfig', 'nodes']

        Attributes:
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
            discovery_enabled (bool | Unset):
            platform_service (bool | Unset):
            scope (ScopeEnum | Unset): * `system` - System
                * `user` - User
            kind (BlockKindEnum | Unset): * `dockerapp` - Docker App
                * `linuxapp` - Linux App
                * `k8sapp` - Kubernetes App
                * `k8sappinstance` - Kubernetes App Instance
                * `k8scluster` - Kubernetes Cluster
                * `library` - Block Library
                * `generic` - Anything
            archived (bool | Unset): Archived objects are not shown in the UI and are not managed by the API.
            archived_at (datetime.datetime | None | Unset):
            archived_reason (None | str | Unset): The reason why the object was archived
            criticality (BlankEnum | CriticalityEnum | None | Unset): Criticality level. Null = inherit from workspace, then
                org. Explicit value overrides inheritance.

                * `high` - High
                * `medium` - Medium
                * `low` - Low
            target_availability (None | str | Unset): Target availability in % (overrides SystemConfig default). Null = use
                SystemConfig DEFAULT_TARGET_AVAILABILITY.
            actual_availability (str | Unset): Calculated actual availability as yearly average in %
            slo_target (None | str | Unset): Internal SLO target in %. Null = use SystemConfig DEFAULT_SLO_TARGET
            slo_availability (str | Unset): Calculated SLO availability in % (updated in reconcile)
            sla_target (None | str | Unset): Contractual SLA target in %. Null = use SystemConfig DEFAULT_SLA_TARGET
            sla_availability (str | Unset): Calculated SLA availability in % (updated in reconcile)
            icon_url (None | str | Unset):
            type_ (None | str | Unset):
            flavor (None | str | Unset):
            version (None | str | Unset):
            checksum (None | str | Unset):
            from_block (None | str | Unset):
            app_version (None | str | Unset):
            supports_ha (bool | Unset):
            license_ (None | str | Unset):
            license_url (None | str | Unset):
            website_url (None | str | Unset):
            git_repository_url (None | str | Unset):
            documentation_url (None | str | Unset):
            releases_url (None | str | Unset):
            description (None | str | Unset):
            config (Any | Unset):
            full_spec (Any | Unset):
            user_spec (Any | Unset):
            actions (Any | Unset):
            is_behind_stable (bool | Unset):
            latest_stable (None | str | Unset):
            template (bool | Unset):  Default: False.
            registry_url (None | str | Unset):
            template_block (None | Unset | UUID):
            block_poly_raw (str | Unset): Raw block.poly YAML content (template blocks only)
            changelog_poly_raw (str | Unset): Raw CHANGELOG.poly YAML content (template blocks only)
            readme_md_raw (str | Unset): Raw README.md content (template blocks only)
            examples_poly_raw (None | str | Unset): Raw examples.poly YAML content (template blocks only)
            auto_rollout (bool | Unset): If False, reconciliation will not automatically enqueue rollout items for this
                block
            created_by_brc (None | Unset | UUID): BlockRolloutConfig that created this block automatically, if any.
            created_by_component (BlankEnum | CreatedByComponentEnum | None | Unset): Component that created this object:
                cli, operator, or api.

                * `cli` - CLI
                * `operator` - Operator
                * `api` - API
    """

    name: str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: ProviderEnum | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    discovery_enabled: bool | Unset = UNSET
    platform_service: bool | Unset = UNSET
    scope: ScopeEnum | Unset = UNSET
    kind: BlockKindEnum | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    criticality: BlankEnum | CriticalityEnum | None | Unset = UNSET
    target_availability: None | str | Unset = UNSET
    actual_availability: str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_availability: str | Unset = UNSET
    icon_url: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    flavor: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    checksum: None | str | Unset = UNSET
    from_block: None | str | Unset = UNSET
    app_version: None | str | Unset = UNSET
    supports_ha: bool | Unset = UNSET
    license_: None | str | Unset = UNSET
    license_url: None | str | Unset = UNSET
    website_url: None | str | Unset = UNSET
    git_repository_url: None | str | Unset = UNSET
    documentation_url: None | str | Unset = UNSET
    releases_url: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    config: Any | Unset = UNSET
    full_spec: Any | Unset = UNSET
    user_spec: Any | Unset = UNSET
    actions: Any | Unset = UNSET
    is_behind_stable: bool | Unset = UNSET
    latest_stable: None | str | Unset = UNSET
    template: bool | Unset = False
    registry_url: None | str | Unset = UNSET
    template_block: None | Unset | UUID = UNSET
    block_poly_raw: str | Unset = UNSET
    changelog_poly_raw: str | Unset = UNSET
    readme_md_raw: str | Unset = UNSET
    examples_poly_raw: None | str | Unset = UNSET
    auto_rollout: bool | Unset = UNSET
    created_by_brc: None | Unset | UUID = UNSET
    created_by_component: BlankEnum | CreatedByComponentEnum | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        discovery_enabled = self.discovery_enabled

        platform_service = self.platform_service

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

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

        criticality: None | str | Unset
        if isinstance(self.criticality, Unset):
            criticality = UNSET
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        elif isinstance(self.criticality, str):
            criticality = self.criticality
        else:
            criticality = self.criticality

        target_availability: None | str | Unset
        if isinstance(self.target_availability, Unset):
            target_availability = UNSET
        else:
            target_availability = self.target_availability

        actual_availability = self.actual_availability

        slo_target: None | str | Unset
        if isinstance(self.slo_target, Unset):
            slo_target = UNSET
        else:
            slo_target = self.slo_target

        slo_availability = self.slo_availability

        sla_target: None | str | Unset
        if isinstance(self.sla_target, Unset):
            sla_target = UNSET
        else:
            sla_target = self.sla_target

        sla_availability = self.sla_availability

        icon_url: None | str | Unset
        if isinstance(self.icon_url, Unset):
            icon_url = UNSET
        else:
            icon_url = self.icon_url

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        flavor: None | str | Unset
        if isinstance(self.flavor, Unset):
            flavor = UNSET
        else:
            flavor = self.flavor

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        checksum: None | str | Unset
        if isinstance(self.checksum, Unset):
            checksum = UNSET
        else:
            checksum = self.checksum

        from_block: None | str | Unset
        if isinstance(self.from_block, Unset):
            from_block = UNSET
        else:
            from_block = self.from_block

        app_version: None | str | Unset
        if isinstance(self.app_version, Unset):
            app_version = UNSET
        else:
            app_version = self.app_version

        supports_ha = self.supports_ha

        license_: None | str | Unset
        if isinstance(self.license_, Unset):
            license_ = UNSET
        else:
            license_ = self.license_

        license_url: None | str | Unset
        if isinstance(self.license_url, Unset):
            license_url = UNSET
        else:
            license_url = self.license_url

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        git_repository_url: None | str | Unset
        if isinstance(self.git_repository_url, Unset):
            git_repository_url = UNSET
        else:
            git_repository_url = self.git_repository_url

        documentation_url: None | str | Unset
        if isinstance(self.documentation_url, Unset):
            documentation_url = UNSET
        else:
            documentation_url = self.documentation_url

        releases_url: None | str | Unset
        if isinstance(self.releases_url, Unset):
            releases_url = UNSET
        else:
            releases_url = self.releases_url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        config = self.config

        full_spec = self.full_spec

        user_spec = self.user_spec

        actions = self.actions

        is_behind_stable = self.is_behind_stable

        latest_stable: None | str | Unset
        if isinstance(self.latest_stable, Unset):
            latest_stable = UNSET
        else:
            latest_stable = self.latest_stable

        template = self.template

        registry_url: None | str | Unset
        if isinstance(self.registry_url, Unset):
            registry_url = UNSET
        else:
            registry_url = self.registry_url

        template_block: None | str | Unset
        if isinstance(self.template_block, Unset):
            template_block = UNSET
        elif isinstance(self.template_block, UUID):
            template_block = str(self.template_block)
        else:
            template_block = self.template_block

        block_poly_raw = self.block_poly_raw

        changelog_poly_raw = self.changelog_poly_raw

        readme_md_raw = self.readme_md_raw

        examples_poly_raw: None | str | Unset
        if isinstance(self.examples_poly_raw, Unset):
            examples_poly_raw = UNSET
        else:
            examples_poly_raw = self.examples_poly_raw

        auto_rollout = self.auto_rollout

        created_by_brc: None | str | Unset
        if isinstance(self.created_by_brc, Unset):
            created_by_brc = UNSET
        elif isinstance(self.created_by_brc, UUID):
            created_by_brc = str(self.created_by_brc)
        else:
            created_by_brc = self.created_by_brc

        created_by_component: None | str | Unset
        if isinstance(self.created_by_component, Unset):
            created_by_component = UNSET
        elif isinstance(self.created_by_component, str):
            created_by_component = self.created_by_component
        elif isinstance(self.created_by_component, str):
            created_by_component = self.created_by_component
        else:
            created_by_component = self.created_by_component

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if discovery_enabled is not UNSET:
            field_dict["discovery_enabled"] = discovery_enabled
        if platform_service is not UNSET:
            field_dict["platform_service"] = platform_service
        if scope is not UNSET:
            field_dict["scope"] = scope
        if kind is not UNSET:
            field_dict["kind"] = kind
        if archived is not UNSET:
            field_dict["archived"] = archived
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if archived_reason is not UNSET:
            field_dict["archived_reason"] = archived_reason
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if target_availability is not UNSET:
            field_dict["target_availability"] = target_availability
        if actual_availability is not UNSET:
            field_dict["actual_availability"] = actual_availability
        if slo_target is not UNSET:
            field_dict["slo_target"] = slo_target
        if slo_availability is not UNSET:
            field_dict["slo_availability"] = slo_availability
        if sla_target is not UNSET:
            field_dict["sla_target"] = sla_target
        if sla_availability is not UNSET:
            field_dict["sla_availability"] = sla_availability
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if flavor is not UNSET:
            field_dict["flavor"] = flavor
        if version is not UNSET:
            field_dict["version"] = version
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if from_block is not UNSET:
            field_dict["from_block"] = from_block
        if app_version is not UNSET:
            field_dict["app_version"] = app_version
        if supports_ha is not UNSET:
            field_dict["supports_ha"] = supports_ha
        if license_ is not UNSET:
            field_dict["license"] = license_
        if license_url is not UNSET:
            field_dict["license_url"] = license_url
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if git_repository_url is not UNSET:
            field_dict["git_repository_url"] = git_repository_url
        if documentation_url is not UNSET:
            field_dict["documentation_url"] = documentation_url
        if releases_url is not UNSET:
            field_dict["releases_url"] = releases_url
        if description is not UNSET:
            field_dict["description"] = description
        if config is not UNSET:
            field_dict["config"] = config
        if full_spec is not UNSET:
            field_dict["full_spec"] = full_spec
        if user_spec is not UNSET:
            field_dict["user_spec"] = user_spec
        if actions is not UNSET:
            field_dict["actions"] = actions
        if is_behind_stable is not UNSET:
            field_dict["is_behind_stable"] = is_behind_stable
        if latest_stable is not UNSET:
            field_dict["latest_stable"] = latest_stable
        if template is not UNSET:
            field_dict["template"] = template
        if registry_url is not UNSET:
            field_dict["registry_url"] = registry_url
        if template_block is not UNSET:
            field_dict["template_block"] = template_block
        if block_poly_raw is not UNSET:
            field_dict["block_poly_raw"] = block_poly_raw
        if changelog_poly_raw is not UNSET:
            field_dict["changelog_poly_raw"] = changelog_poly_raw
        if readme_md_raw is not UNSET:
            field_dict["readme_md_raw"] = readme_md_raw
        if examples_poly_raw is not UNSET:
            field_dict["examples_poly_raw"] = examples_poly_raw
        if auto_rollout is not UNSET:
            field_dict["auto_rollout"] = auto_rollout
        if created_by_brc is not UNSET:
            field_dict["created_by_brc"] = created_by_brc
        if created_by_component is not UNSET:
            field_dict["created_by_component"] = created_by_component

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

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

        if not isinstance(self.discovery_enabled, Unset):
            files.append(("discovery_enabled", (None, str(self.discovery_enabled).encode(), "text/plain")))

        if not isinstance(self.platform_service, Unset):
            files.append(("platform_service", (None, str(self.platform_service).encode(), "text/plain")))

        if not isinstance(self.scope, Unset):
            files.append(("scope", (None, str(self.scope).encode(), "text/plain")))

        if not isinstance(self.kind, Unset):
            files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

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

        if not isinstance(self.criticality, Unset):
            if isinstance(self.criticality, str):
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))
            elif isinstance(self.criticality, str):
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))
            else:
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))

        if not isinstance(self.target_availability, Unset):
            if isinstance(self.target_availability, str):
                files.append(("target_availability", (None, str(self.target_availability).encode(), "text/plain")))
            else:
                files.append(("target_availability", (None, str(self.target_availability).encode(), "text/plain")))

        if not isinstance(self.actual_availability, Unset):
            files.append(("actual_availability", (None, str(self.actual_availability).encode(), "text/plain")))

        if not isinstance(self.slo_target, Unset):
            if isinstance(self.slo_target, str):
                files.append(("slo_target", (None, str(self.slo_target).encode(), "text/plain")))
            else:
                files.append(("slo_target", (None, str(self.slo_target).encode(), "text/plain")))

        if not isinstance(self.slo_availability, Unset):
            files.append(("slo_availability", (None, str(self.slo_availability).encode(), "text/plain")))

        if not isinstance(self.sla_target, Unset):
            if isinstance(self.sla_target, str):
                files.append(("sla_target", (None, str(self.sla_target).encode(), "text/plain")))
            else:
                files.append(("sla_target", (None, str(self.sla_target).encode(), "text/plain")))

        if not isinstance(self.sla_availability, Unset):
            files.append(("sla_availability", (None, str(self.sla_availability).encode(), "text/plain")))

        if not isinstance(self.icon_url, Unset):
            if isinstance(self.icon_url, str):
                files.append(("icon_url", (None, str(self.icon_url).encode(), "text/plain")))
            else:
                files.append(("icon_url", (None, str(self.icon_url).encode(), "text/plain")))

        if not isinstance(self.type_, Unset):
            if isinstance(self.type_, str):
                files.append(("type", (None, str(self.type_).encode(), "text/plain")))
            else:
                files.append(("type", (None, str(self.type_).encode(), "text/plain")))

        if not isinstance(self.flavor, Unset):
            if isinstance(self.flavor, str):
                files.append(("flavor", (None, str(self.flavor).encode(), "text/plain")))
            else:
                files.append(("flavor", (None, str(self.flavor).encode(), "text/plain")))

        if not isinstance(self.version, Unset):
            if isinstance(self.version, str):
                files.append(("version", (None, str(self.version).encode(), "text/plain")))
            else:
                files.append(("version", (None, str(self.version).encode(), "text/plain")))

        if not isinstance(self.checksum, Unset):
            if isinstance(self.checksum, str):
                files.append(("checksum", (None, str(self.checksum).encode(), "text/plain")))
            else:
                files.append(("checksum", (None, str(self.checksum).encode(), "text/plain")))

        if not isinstance(self.from_block, Unset):
            if isinstance(self.from_block, str):
                files.append(("from_block", (None, str(self.from_block).encode(), "text/plain")))
            else:
                files.append(("from_block", (None, str(self.from_block).encode(), "text/plain")))

        if not isinstance(self.app_version, Unset):
            if isinstance(self.app_version, str):
                files.append(("app_version", (None, str(self.app_version).encode(), "text/plain")))
            else:
                files.append(("app_version", (None, str(self.app_version).encode(), "text/plain")))

        if not isinstance(self.supports_ha, Unset):
            files.append(("supports_ha", (None, str(self.supports_ha).encode(), "text/plain")))

        if not isinstance(self.license_, Unset):
            if isinstance(self.license_, str):
                files.append(("license", (None, str(self.license_).encode(), "text/plain")))
            else:
                files.append(("license", (None, str(self.license_).encode(), "text/plain")))

        if not isinstance(self.license_url, Unset):
            if isinstance(self.license_url, str):
                files.append(("license_url", (None, str(self.license_url).encode(), "text/plain")))
            else:
                files.append(("license_url", (None, str(self.license_url).encode(), "text/plain")))

        if not isinstance(self.website_url, Unset):
            if isinstance(self.website_url, str):
                files.append(("website_url", (None, str(self.website_url).encode(), "text/plain")))
            else:
                files.append(("website_url", (None, str(self.website_url).encode(), "text/plain")))

        if not isinstance(self.git_repository_url, Unset):
            if isinstance(self.git_repository_url, str):
                files.append(("git_repository_url", (None, str(self.git_repository_url).encode(), "text/plain")))
            else:
                files.append(("git_repository_url", (None, str(self.git_repository_url).encode(), "text/plain")))

        if not isinstance(self.documentation_url, Unset):
            if isinstance(self.documentation_url, str):
                files.append(("documentation_url", (None, str(self.documentation_url).encode(), "text/plain")))
            else:
                files.append(("documentation_url", (None, str(self.documentation_url).encode(), "text/plain")))

        if not isinstance(self.releases_url, Unset):
            if isinstance(self.releases_url, str):
                files.append(("releases_url", (None, str(self.releases_url).encode(), "text/plain")))
            else:
                files.append(("releases_url", (None, str(self.releases_url).encode(), "text/plain")))

        if not isinstance(self.description, Unset):
            if isinstance(self.description, str):
                files.append(("description", (None, str(self.description).encode(), "text/plain")))
            else:
                files.append(("description", (None, str(self.description).encode(), "text/plain")))

        if not isinstance(self.config, Unset):
            files.append(("config", (None, str(self.config).encode(), "text/plain")))

        if not isinstance(self.full_spec, Unset):
            files.append(("full_spec", (None, str(self.full_spec).encode(), "text/plain")))

        if not isinstance(self.user_spec, Unset):
            files.append(("user_spec", (None, str(self.user_spec).encode(), "text/plain")))

        if not isinstance(self.actions, Unset):
            files.append(("actions", (None, str(self.actions).encode(), "text/plain")))

        if not isinstance(self.is_behind_stable, Unset):
            files.append(("is_behind_stable", (None, str(self.is_behind_stable).encode(), "text/plain")))

        if not isinstance(self.latest_stable, Unset):
            if isinstance(self.latest_stable, str):
                files.append(("latest_stable", (None, str(self.latest_stable).encode(), "text/plain")))
            else:
                files.append(("latest_stable", (None, str(self.latest_stable).encode(), "text/plain")))

        if not isinstance(self.template, Unset):
            files.append(("template", (None, str(self.template).encode(), "text/plain")))

        if not isinstance(self.registry_url, Unset):
            if isinstance(self.registry_url, str):
                files.append(("registry_url", (None, str(self.registry_url).encode(), "text/plain")))
            else:
                files.append(("registry_url", (None, str(self.registry_url).encode(), "text/plain")))

        if not isinstance(self.template_block, Unset):
            if isinstance(self.template_block, UUID):
                files.append(("template_block", (None, str(self.template_block), "text/plain")))
            else:
                files.append(("template_block", (None, str(self.template_block).encode(), "text/plain")))

        if not isinstance(self.block_poly_raw, Unset):
            files.append(("block_poly_raw", (None, str(self.block_poly_raw).encode(), "text/plain")))

        if not isinstance(self.changelog_poly_raw, Unset):
            files.append(("changelog_poly_raw", (None, str(self.changelog_poly_raw).encode(), "text/plain")))

        if not isinstance(self.readme_md_raw, Unset):
            files.append(("readme_md_raw", (None, str(self.readme_md_raw).encode(), "text/plain")))

        if not isinstance(self.examples_poly_raw, Unset):
            if isinstance(self.examples_poly_raw, str):
                files.append(("examples_poly_raw", (None, str(self.examples_poly_raw).encode(), "text/plain")))
            else:
                files.append(("examples_poly_raw", (None, str(self.examples_poly_raw).encode(), "text/plain")))

        if not isinstance(self.auto_rollout, Unset):
            files.append(("auto_rollout", (None, str(self.auto_rollout).encode(), "text/plain")))

        if not isinstance(self.created_by_brc, Unset):
            if isinstance(self.created_by_brc, UUID):
                files.append(("created_by_brc", (None, str(self.created_by_brc), "text/plain")))
            else:
                files.append(("created_by_brc", (None, str(self.created_by_brc).encode(), "text/plain")))

        if not isinstance(self.created_by_component, Unset):
            if isinstance(self.created_by_component, str):
                files.append(("created_by_component", (None, str(self.created_by_component).encode(), "text/plain")))
            elif isinstance(self.created_by_component, str):
                files.append(("created_by_component", (None, str(self.created_by_component).encode(), "text/plain")))
            else:
                files.append(("created_by_component", (None, str(self.created_by_component).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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

        discovery_enabled = d.pop("discovery_enabled", UNSET)

        platform_service = d.pop("platform_service", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: ScopeEnum | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_scope_enum(_scope)

        _kind = d.pop("kind", UNSET)
        kind: BlockKindEnum | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_block_kind_enum(_kind)

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

        def _parse_target_availability(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target_availability = _parse_target_availability(d.pop("target_availability", UNSET))

        actual_availability = d.pop("actual_availability", UNSET)

        def _parse_slo_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        slo_target = _parse_slo_target(d.pop("slo_target", UNSET))

        slo_availability = d.pop("slo_availability", UNSET)

        def _parse_sla_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sla_target = _parse_sla_target(d.pop("sla_target", UNSET))

        sla_availability = d.pop("sla_availability", UNSET)

        def _parse_icon_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon_url = _parse_icon_url(d.pop("icon_url", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_flavor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flavor = _parse_flavor(d.pop("flavor", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_checksum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checksum = _parse_checksum(d.pop("checksum", UNSET))

        def _parse_from_block(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_block = _parse_from_block(d.pop("from_block", UNSET))

        def _parse_app_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_version = _parse_app_version(d.pop("app_version", UNSET))

        supports_ha = d.pop("supports_ha", UNSET)

        def _parse_license_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        license_ = _parse_license_(d.pop("license", UNSET))

        def _parse_license_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        license_url = _parse_license_url(d.pop("license_url", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        def _parse_git_repository_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        git_repository_url = _parse_git_repository_url(d.pop("git_repository_url", UNSET))

        def _parse_documentation_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        documentation_url = _parse_documentation_url(d.pop("documentation_url", UNSET))

        def _parse_releases_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        releases_url = _parse_releases_url(d.pop("releases_url", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        config = d.pop("config", UNSET)

        full_spec = d.pop("full_spec", UNSET)

        user_spec = d.pop("user_spec", UNSET)

        actions = d.pop("actions", UNSET)

        is_behind_stable = d.pop("is_behind_stable", UNSET)

        def _parse_latest_stable(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_stable = _parse_latest_stable(d.pop("latest_stable", UNSET))

        template = d.pop("template", UNSET)

        def _parse_registry_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registry_url = _parse_registry_url(d.pop("registry_url", UNSET))

        def _parse_template_block(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                template_block_type_0 = UUID(data)

                return template_block_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        template_block = _parse_template_block(d.pop("template_block", UNSET))

        block_poly_raw = d.pop("block_poly_raw", UNSET)

        changelog_poly_raw = d.pop("changelog_poly_raw", UNSET)

        readme_md_raw = d.pop("readme_md_raw", UNSET)

        def _parse_examples_poly_raw(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        examples_poly_raw = _parse_examples_poly_raw(d.pop("examples_poly_raw", UNSET))

        auto_rollout = d.pop("auto_rollout", UNSET)

        def _parse_created_by_brc(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_brc_type_0 = UUID(data)

                return created_by_brc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by_brc = _parse_created_by_brc(d.pop("created_by_brc", UNSET))

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

        block_request = cls(
            name=name,
            display_name=display_name,
            labels=labels,
            annotations=annotations,
            debug_mode=debug_mode,
            provider=provider,
            provider_reference=provider_reference,
            provider_id=provider_id,
            reconciliation_enabled=reconciliation_enabled,
            discovery_enabled=discovery_enabled,
            platform_service=platform_service,
            scope=scope,
            kind=kind,
            archived=archived,
            archived_at=archived_at,
            archived_reason=archived_reason,
            criticality=criticality,
            target_availability=target_availability,
            actual_availability=actual_availability,
            slo_target=slo_target,
            slo_availability=slo_availability,
            sla_target=sla_target,
            sla_availability=sla_availability,
            icon_url=icon_url,
            type_=type_,
            flavor=flavor,
            version=version,
            checksum=checksum,
            from_block=from_block,
            app_version=app_version,
            supports_ha=supports_ha,
            license_=license_,
            license_url=license_url,
            website_url=website_url,
            git_repository_url=git_repository_url,
            documentation_url=documentation_url,
            releases_url=releases_url,
            description=description,
            config=config,
            full_spec=full_spec,
            user_spec=user_spec,
            actions=actions,
            is_behind_stable=is_behind_stable,
            latest_stable=latest_stable,
            template=template,
            registry_url=registry_url,
            template_block=template_block,
            block_poly_raw=block_poly_raw,
            changelog_poly_raw=changelog_poly_raw,
            readme_md_raw=readme_md_raw,
            examples_poly_raw=examples_poly_raw,
            auto_rollout=auto_rollout,
            created_by_brc=created_by_brc,
            created_by_component=created_by_component,
        )

        block_request.additional_properties = d
        return block_request

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
