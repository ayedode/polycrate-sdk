from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.registrar_tld_price_detail_request_created_by_component_type_1 import (
    RegistrarTLDPriceDetailRequestCreatedByComponentType1,
    check_registrar_tld_price_detail_request_created_by_component_type_1,
)
from ..models.registrar_tld_price_detail_request_created_by_component_type_2_type_1 import (
    RegistrarTLDPriceDetailRequestCreatedByComponentType2Type1,
    check_registrar_tld_price_detail_request_created_by_component_type_2_type_1,
)
from ..models.registrar_tld_price_detail_request_created_by_component_type_3_type_1 import (
    RegistrarTLDPriceDetailRequestCreatedByComponentType3Type1,
    check_registrar_tld_price_detail_request_created_by_component_type_3_type_1,
)
from ..models.registrar_tld_price_detail_request_criticality_type_1 import (
    RegistrarTLDPriceDetailRequestCriticalityType1,
    check_registrar_tld_price_detail_request_criticality_type_1,
)
from ..models.registrar_tld_price_detail_request_criticality_type_2_type_1 import (
    RegistrarTLDPriceDetailRequestCriticalityType2Type1,
    check_registrar_tld_price_detail_request_criticality_type_2_type_1,
)
from ..models.registrar_tld_price_detail_request_criticality_type_3_type_1 import (
    RegistrarTLDPriceDetailRequestCriticalityType3Type1,
    check_registrar_tld_price_detail_request_criticality_type_3_type_1,
)
from ..models.registrar_tld_price_detail_request_kind import (
    RegistrarTLDPriceDetailRequestKind,
    check_registrar_tld_price_detail_request_kind,
)
from ..models.registrar_tld_price_detail_request_provider import (
    RegistrarTLDPriceDetailRequestProvider,
    check_registrar_tld_price_detail_request_provider,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RegistrarTLDPriceDetailRequest")


@_attrs_define
class RegistrarTLDPriceDetailRequest:
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
            tld (str): TLD without leading dot.
            name (str | Unset): Object name
            registrar_id (UUID | Unset):
            display_name (None | str | Unset): The display name is used to display the object in the UI. It can be different
                from the name.
            labels (Any | Unset):
            annotations (Any | Unset):
            debug_mode (bool | Unset): Persists all Object Logs in the database
            provider (RegistrarTLDPriceDetailRequestProvider | Unset): * `loopback` - Loopback
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
            kind (RegistrarTLDPriceDetailRequestKind | Unset): * `generic` - Generic
            tolerations (Any | Unset): Tolerations match conditions. If a toleration for a condition exists for an object,
                the condition will not be applied.
            archived (bool | Unset): Archived objects are not shown in the UI and are not managed by the API.
            archived_at (datetime.datetime | None | Unset):
            archived_reason (None | str | Unset): The reason why the object was archived
            created_by_component (None | RegistrarTLDPriceDetailRequestCreatedByComponentType1 |
                RegistrarTLDPriceDetailRequestCreatedByComponentType2Type1 |
                RegistrarTLDPriceDetailRequestCreatedByComponentType3Type1 | Unset): Component that created this object: cli,
                operator, or api.

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
            criticality (None | RegistrarTLDPriceDetailRequestCriticalityType1 |
                RegistrarTLDPriceDetailRequestCriticalityType2Type1 | RegistrarTLDPriceDetailRequestCriticalityType3Type1 |
                Unset): Criticality level. Null = inherit from workspace, then org. Explicit value overrides inheritance.

                * `high` - High
                * `medium` - Medium
                * `low` - Low
            managed_by_object_id (None | str | Unset):
            platform_dns_record_created (bool | Unset):
            provider_status (str | Unset):
            active (bool | Unset): Staff switch: we sell this TLD. Sync never writes this field.
            offerable (bool | Unset): Informative OpenProvider list flag. Not the sales filter.
            domicile_available (bool | Unset):
            transfer_available (bool | Unset):
            trade_available (bool | Unset):
            renew_available (bool | Unset):
            private_whois_allowed (bool | Unset):
            min_period (int | None | Unset):
            max_period (int | None | Unset):
            currency (str | Unset):
            ek_create (None | str | Unset):
            ek_renew (None | str | Unset):
            ek_transfer (None | str | Unset):
            ek_restore (None | str | Unset):
            ek_soft_restore (None | str | Unset):
            ek_setup (None | str | Unset):
            ek_update (None | str | Unset):
            ek_trade (None | str | Unset):
            ek_domicile (None | str | Unset):
            vk_create (None | str | Unset):
            vk_renew (None | str | Unset):
            vk_transfer (None | str | Unset):
            vk_domicile (None | str | Unset):
            prices_extra (Any | Unset):
            last_ek_synced_at (datetime.datetime | None | Unset):
            archived_by (int | None | Unset): The user who archived the object
            managed_by_content_type (int | None | Unset):
            modified_by_user (int | None | Unset): The user who last modified the object
            created_by_user (int | None | Unset): The user who created the object
    """

    tld: str
    name: str | Unset = UNSET
    registrar_id: UUID | Unset = UNSET
    display_name: None | str | Unset = UNSET
    labels: Any | Unset = UNSET
    annotations: Any | Unset = UNSET
    debug_mode: bool | Unset = UNSET
    provider: RegistrarTLDPriceDetailRequestProvider | Unset = UNSET
    provider_reference: None | str | Unset = UNSET
    provider_id: None | str | Unset = UNSET
    reconciliation_enabled: bool | Unset = UNSET
    last_reconciliation_duration_seconds: float | None | Unset = UNSET
    platform_service: bool | Unset = UNSET
    kind: RegistrarTLDPriceDetailRequestKind | Unset = UNSET
    tolerations: Any | Unset = UNSET
    archived: bool | Unset = UNSET
    archived_at: datetime.datetime | None | Unset = UNSET
    archived_reason: None | str | Unset = UNSET
    created_by_component: (
        None
        | RegistrarTLDPriceDetailRequestCreatedByComponentType1
        | RegistrarTLDPriceDetailRequestCreatedByComponentType2Type1
        | RegistrarTLDPriceDetailRequestCreatedByComponentType3Type1
        | Unset
    ) = UNSET
    target_availability: None | str | Unset = UNSET
    slo_target: None | str | Unset = UNSET
    slo_window_days: int | None | Unset = UNSET
    slo_availability: str | Unset = UNSET
    sla_target: None | str | Unset = UNSET
    sla_window_days: int | None | Unset = UNSET
    sla_availability: str | Unset = UNSET
    criticality: (
        None
        | RegistrarTLDPriceDetailRequestCriticalityType1
        | RegistrarTLDPriceDetailRequestCriticalityType2Type1
        | RegistrarTLDPriceDetailRequestCriticalityType3Type1
        | Unset
    ) = UNSET
    managed_by_object_id: None | str | Unset = UNSET
    platform_dns_record_created: bool | Unset = UNSET
    provider_status: str | Unset = UNSET
    active: bool | Unset = UNSET
    offerable: bool | Unset = UNSET
    domicile_available: bool | Unset = UNSET
    transfer_available: bool | Unset = UNSET
    trade_available: bool | Unset = UNSET
    renew_available: bool | Unset = UNSET
    private_whois_allowed: bool | Unset = UNSET
    min_period: int | None | Unset = UNSET
    max_period: int | None | Unset = UNSET
    currency: str | Unset = UNSET
    ek_create: None | str | Unset = UNSET
    ek_renew: None | str | Unset = UNSET
    ek_transfer: None | str | Unset = UNSET
    ek_restore: None | str | Unset = UNSET
    ek_soft_restore: None | str | Unset = UNSET
    ek_setup: None | str | Unset = UNSET
    ek_update: None | str | Unset = UNSET
    ek_trade: None | str | Unset = UNSET
    ek_domicile: None | str | Unset = UNSET
    vk_create: None | str | Unset = UNSET
    vk_renew: None | str | Unset = UNSET
    vk_transfer: None | str | Unset = UNSET
    vk_domicile: None | str | Unset = UNSET
    prices_extra: Any | Unset = UNSET
    last_ek_synced_at: datetime.datetime | None | Unset = UNSET
    archived_by: int | None | Unset = UNSET
    managed_by_content_type: int | None | Unset = UNSET
    modified_by_user: int | None | Unset = UNSET
    created_by_user: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tld = self.tld

        name = self.name

        registrar_id: str | Unset = UNSET
        if not isinstance(self.registrar_id, Unset):
            registrar_id = str(self.registrar_id)

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

        provider_status = self.provider_status

        active = self.active

        offerable = self.offerable

        domicile_available = self.domicile_available

        transfer_available = self.transfer_available

        trade_available = self.trade_available

        renew_available = self.renew_available

        private_whois_allowed = self.private_whois_allowed

        min_period: int | None | Unset
        if isinstance(self.min_period, Unset):
            min_period = UNSET
        else:
            min_period = self.min_period

        max_period: int | None | Unset
        if isinstance(self.max_period, Unset):
            max_period = UNSET
        else:
            max_period = self.max_period

        currency = self.currency

        ek_create: None | str | Unset
        if isinstance(self.ek_create, Unset):
            ek_create = UNSET
        else:
            ek_create = self.ek_create

        ek_renew: None | str | Unset
        if isinstance(self.ek_renew, Unset):
            ek_renew = UNSET
        else:
            ek_renew = self.ek_renew

        ek_transfer: None | str | Unset
        if isinstance(self.ek_transfer, Unset):
            ek_transfer = UNSET
        else:
            ek_transfer = self.ek_transfer

        ek_restore: None | str | Unset
        if isinstance(self.ek_restore, Unset):
            ek_restore = UNSET
        else:
            ek_restore = self.ek_restore

        ek_soft_restore: None | str | Unset
        if isinstance(self.ek_soft_restore, Unset):
            ek_soft_restore = UNSET
        else:
            ek_soft_restore = self.ek_soft_restore

        ek_setup: None | str | Unset
        if isinstance(self.ek_setup, Unset):
            ek_setup = UNSET
        else:
            ek_setup = self.ek_setup

        ek_update: None | str | Unset
        if isinstance(self.ek_update, Unset):
            ek_update = UNSET
        else:
            ek_update = self.ek_update

        ek_trade: None | str | Unset
        if isinstance(self.ek_trade, Unset):
            ek_trade = UNSET
        else:
            ek_trade = self.ek_trade

        ek_domicile: None | str | Unset
        if isinstance(self.ek_domicile, Unset):
            ek_domicile = UNSET
        else:
            ek_domicile = self.ek_domicile

        vk_create: None | str | Unset
        if isinstance(self.vk_create, Unset):
            vk_create = UNSET
        else:
            vk_create = self.vk_create

        vk_renew: None | str | Unset
        if isinstance(self.vk_renew, Unset):
            vk_renew = UNSET
        else:
            vk_renew = self.vk_renew

        vk_transfer: None | str | Unset
        if isinstance(self.vk_transfer, Unset):
            vk_transfer = UNSET
        else:
            vk_transfer = self.vk_transfer

        vk_domicile: None | str | Unset
        if isinstance(self.vk_domicile, Unset):
            vk_domicile = UNSET
        else:
            vk_domicile = self.vk_domicile

        prices_extra = self.prices_extra

        last_ek_synced_at: None | str | Unset
        if isinstance(self.last_ek_synced_at, Unset):
            last_ek_synced_at = UNSET
        elif isinstance(self.last_ek_synced_at, datetime.datetime):
            last_ek_synced_at = self.last_ek_synced_at.isoformat()
        else:
            last_ek_synced_at = self.last_ek_synced_at

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tld": tld,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if registrar_id is not UNSET:
            field_dict["registrar_id"] = registrar_id
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
        if provider_status is not UNSET:
            field_dict["provider_status"] = provider_status
        if active is not UNSET:
            field_dict["active"] = active
        if offerable is not UNSET:
            field_dict["offerable"] = offerable
        if domicile_available is not UNSET:
            field_dict["domicile_available"] = domicile_available
        if transfer_available is not UNSET:
            field_dict["transfer_available"] = transfer_available
        if trade_available is not UNSET:
            field_dict["trade_available"] = trade_available
        if renew_available is not UNSET:
            field_dict["renew_available"] = renew_available
        if private_whois_allowed is not UNSET:
            field_dict["private_whois_allowed"] = private_whois_allowed
        if min_period is not UNSET:
            field_dict["min_period"] = min_period
        if max_period is not UNSET:
            field_dict["max_period"] = max_period
        if currency is not UNSET:
            field_dict["currency"] = currency
        if ek_create is not UNSET:
            field_dict["ek_create"] = ek_create
        if ek_renew is not UNSET:
            field_dict["ek_renew"] = ek_renew
        if ek_transfer is not UNSET:
            field_dict["ek_transfer"] = ek_transfer
        if ek_restore is not UNSET:
            field_dict["ek_restore"] = ek_restore
        if ek_soft_restore is not UNSET:
            field_dict["ek_soft_restore"] = ek_soft_restore
        if ek_setup is not UNSET:
            field_dict["ek_setup"] = ek_setup
        if ek_update is not UNSET:
            field_dict["ek_update"] = ek_update
        if ek_trade is not UNSET:
            field_dict["ek_trade"] = ek_trade
        if ek_domicile is not UNSET:
            field_dict["ek_domicile"] = ek_domicile
        if vk_create is not UNSET:
            field_dict["vk_create"] = vk_create
        if vk_renew is not UNSET:
            field_dict["vk_renew"] = vk_renew
        if vk_transfer is not UNSET:
            field_dict["vk_transfer"] = vk_transfer
        if vk_domicile is not UNSET:
            field_dict["vk_domicile"] = vk_domicile
        if prices_extra is not UNSET:
            field_dict["prices_extra"] = prices_extra
        if last_ek_synced_at is not UNSET:
            field_dict["last_ek_synced_at"] = last_ek_synced_at
        if archived_by is not UNSET:
            field_dict["archived_by"] = archived_by
        if managed_by_content_type is not UNSET:
            field_dict["managed_by_content_type"] = managed_by_content_type
        if modified_by_user is not UNSET:
            field_dict["modified_by_user"] = modified_by_user
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("tld", (None, str(self.tld).encode(), "text/plain")))

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.registrar_id, Unset):
            files.append(("registrar_id", (None, str(self.registrar_id), "text/plain")))

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
            if self.created_by_component is None:
                files.append(("created_by_component", (None, str(self.created_by_component).encode(), "text/plain")))
            elif isinstance(self.created_by_component, str):
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
            if self.criticality is None:
                files.append(("criticality", (None, str(self.criticality).encode(), "text/plain")))
            elif isinstance(self.criticality, str):
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

        if not isinstance(self.provider_status, Unset):
            files.append(("provider_status", (None, str(self.provider_status).encode(), "text/plain")))

        if not isinstance(self.active, Unset):
            files.append(("active", (None, str(self.active).encode(), "text/plain")))

        if not isinstance(self.offerable, Unset):
            files.append(("offerable", (None, str(self.offerable).encode(), "text/plain")))

        if not isinstance(self.domicile_available, Unset):
            files.append(("domicile_available", (None, str(self.domicile_available).encode(), "text/plain")))

        if not isinstance(self.transfer_available, Unset):
            files.append(("transfer_available", (None, str(self.transfer_available).encode(), "text/plain")))

        if not isinstance(self.trade_available, Unset):
            files.append(("trade_available", (None, str(self.trade_available).encode(), "text/plain")))

        if not isinstance(self.renew_available, Unset):
            files.append(("renew_available", (None, str(self.renew_available).encode(), "text/plain")))

        if not isinstance(self.private_whois_allowed, Unset):
            files.append(("private_whois_allowed", (None, str(self.private_whois_allowed).encode(), "text/plain")))

        if not isinstance(self.min_period, Unset):
            if isinstance(self.min_period, int):
                files.append(("min_period", (None, str(self.min_period).encode(), "text/plain")))
            else:
                files.append(("min_period", (None, str(self.min_period).encode(), "text/plain")))

        if not isinstance(self.max_period, Unset):
            if isinstance(self.max_period, int):
                files.append(("max_period", (None, str(self.max_period).encode(), "text/plain")))
            else:
                files.append(("max_period", (None, str(self.max_period).encode(), "text/plain")))

        if not isinstance(self.currency, Unset):
            files.append(("currency", (None, str(self.currency).encode(), "text/plain")))

        if not isinstance(self.ek_create, Unset):
            if isinstance(self.ek_create, str):
                files.append(("ek_create", (None, str(self.ek_create).encode(), "text/plain")))
            else:
                files.append(("ek_create", (None, str(self.ek_create).encode(), "text/plain")))

        if not isinstance(self.ek_renew, Unset):
            if isinstance(self.ek_renew, str):
                files.append(("ek_renew", (None, str(self.ek_renew).encode(), "text/plain")))
            else:
                files.append(("ek_renew", (None, str(self.ek_renew).encode(), "text/plain")))

        if not isinstance(self.ek_transfer, Unset):
            if isinstance(self.ek_transfer, str):
                files.append(("ek_transfer", (None, str(self.ek_transfer).encode(), "text/plain")))
            else:
                files.append(("ek_transfer", (None, str(self.ek_transfer).encode(), "text/plain")))

        if not isinstance(self.ek_restore, Unset):
            if isinstance(self.ek_restore, str):
                files.append(("ek_restore", (None, str(self.ek_restore).encode(), "text/plain")))
            else:
                files.append(("ek_restore", (None, str(self.ek_restore).encode(), "text/plain")))

        if not isinstance(self.ek_soft_restore, Unset):
            if isinstance(self.ek_soft_restore, str):
                files.append(("ek_soft_restore", (None, str(self.ek_soft_restore).encode(), "text/plain")))
            else:
                files.append(("ek_soft_restore", (None, str(self.ek_soft_restore).encode(), "text/plain")))

        if not isinstance(self.ek_setup, Unset):
            if isinstance(self.ek_setup, str):
                files.append(("ek_setup", (None, str(self.ek_setup).encode(), "text/plain")))
            else:
                files.append(("ek_setup", (None, str(self.ek_setup).encode(), "text/plain")))

        if not isinstance(self.ek_update, Unset):
            if isinstance(self.ek_update, str):
                files.append(("ek_update", (None, str(self.ek_update).encode(), "text/plain")))
            else:
                files.append(("ek_update", (None, str(self.ek_update).encode(), "text/plain")))

        if not isinstance(self.ek_trade, Unset):
            if isinstance(self.ek_trade, str):
                files.append(("ek_trade", (None, str(self.ek_trade).encode(), "text/plain")))
            else:
                files.append(("ek_trade", (None, str(self.ek_trade).encode(), "text/plain")))

        if not isinstance(self.ek_domicile, Unset):
            if isinstance(self.ek_domicile, str):
                files.append(("ek_domicile", (None, str(self.ek_domicile).encode(), "text/plain")))
            else:
                files.append(("ek_domicile", (None, str(self.ek_domicile).encode(), "text/plain")))

        if not isinstance(self.vk_create, Unset):
            if isinstance(self.vk_create, str):
                files.append(("vk_create", (None, str(self.vk_create).encode(), "text/plain")))
            else:
                files.append(("vk_create", (None, str(self.vk_create).encode(), "text/plain")))

        if not isinstance(self.vk_renew, Unset):
            if isinstance(self.vk_renew, str):
                files.append(("vk_renew", (None, str(self.vk_renew).encode(), "text/plain")))
            else:
                files.append(("vk_renew", (None, str(self.vk_renew).encode(), "text/plain")))

        if not isinstance(self.vk_transfer, Unset):
            if isinstance(self.vk_transfer, str):
                files.append(("vk_transfer", (None, str(self.vk_transfer).encode(), "text/plain")))
            else:
                files.append(("vk_transfer", (None, str(self.vk_transfer).encode(), "text/plain")))

        if not isinstance(self.vk_domicile, Unset):
            if isinstance(self.vk_domicile, str):
                files.append(("vk_domicile", (None, str(self.vk_domicile).encode(), "text/plain")))
            else:
                files.append(("vk_domicile", (None, str(self.vk_domicile).encode(), "text/plain")))

        if not isinstance(self.prices_extra, Unset):
            files.append(("prices_extra", (None, str(self.prices_extra).encode(), "text/plain")))

        if not isinstance(self.last_ek_synced_at, Unset):
            if isinstance(self.last_ek_synced_at, datetime.datetime):
                files.append(("last_ek_synced_at", (None, self.last_ek_synced_at.isoformat().encode(), "text/plain")))
            else:
                files.append(("last_ek_synced_at", (None, str(self.last_ek_synced_at).encode(), "text/plain")))

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

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tld = d.pop("tld")

        name = d.pop("name", UNSET)

        _registrar_id = d.pop("registrar_id", UNSET)
        registrar_id: UUID | Unset
        if isinstance(_registrar_id, Unset):
            registrar_id = UNSET
        else:
            registrar_id = UUID(_registrar_id)

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
        provider: RegistrarTLDPriceDetailRequestProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_registrar_tld_price_detail_request_provider(_provider)

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
        kind: RegistrarTLDPriceDetailRequestKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_registrar_tld_price_detail_request_kind(_kind)

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

        def _parse_created_by_component(
            data: object,
        ) -> (
            None
            | RegistrarTLDPriceDetailRequestCreatedByComponentType1
            | RegistrarTLDPriceDetailRequestCreatedByComponentType2Type1
            | RegistrarTLDPriceDetailRequestCreatedByComponentType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_component_type_1 = check_registrar_tld_price_detail_request_created_by_component_type_1(data)

                return created_by_component_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_component_type_2_type_1 = (
                    check_registrar_tld_price_detail_request_created_by_component_type_2_type_1(data)
                )

                return created_by_component_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_component_type_3_type_1 = (
                    check_registrar_tld_price_detail_request_created_by_component_type_3_type_1(data)
                )

                return created_by_component_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | RegistrarTLDPriceDetailRequestCreatedByComponentType1
                | RegistrarTLDPriceDetailRequestCreatedByComponentType2Type1
                | RegistrarTLDPriceDetailRequestCreatedByComponentType3Type1
                | Unset,
                data,
            )

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

        def _parse_criticality(
            data: object,
        ) -> (
            None
            | RegistrarTLDPriceDetailRequestCriticalityType1
            | RegistrarTLDPriceDetailRequestCriticalityType2Type1
            | RegistrarTLDPriceDetailRequestCriticalityType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_1 = check_registrar_tld_price_detail_request_criticality_type_1(data)

                return criticality_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_2_type_1 = check_registrar_tld_price_detail_request_criticality_type_2_type_1(data)

                return criticality_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                criticality_type_3_type_1 = check_registrar_tld_price_detail_request_criticality_type_3_type_1(data)

                return criticality_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | RegistrarTLDPriceDetailRequestCriticalityType1
                | RegistrarTLDPriceDetailRequestCriticalityType2Type1
                | RegistrarTLDPriceDetailRequestCriticalityType3Type1
                | Unset,
                data,
            )

        criticality = _parse_criticality(d.pop("criticality", UNSET))

        def _parse_managed_by_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        managed_by_object_id = _parse_managed_by_object_id(d.pop("managed_by_object_id", UNSET))

        platform_dns_record_created = d.pop("platform_dns_record_created", UNSET)

        provider_status = d.pop("provider_status", UNSET)

        active = d.pop("active", UNSET)

        offerable = d.pop("offerable", UNSET)

        domicile_available = d.pop("domicile_available", UNSET)

        transfer_available = d.pop("transfer_available", UNSET)

        trade_available = d.pop("trade_available", UNSET)

        renew_available = d.pop("renew_available", UNSET)

        private_whois_allowed = d.pop("private_whois_allowed", UNSET)

        def _parse_min_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_period = _parse_min_period(d.pop("min_period", UNSET))

        def _parse_max_period(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_period = _parse_max_period(d.pop("max_period", UNSET))

        currency = d.pop("currency", UNSET)

        def _parse_ek_create(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_create = _parse_ek_create(d.pop("ek_create", UNSET))

        def _parse_ek_renew(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_renew = _parse_ek_renew(d.pop("ek_renew", UNSET))

        def _parse_ek_transfer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_transfer = _parse_ek_transfer(d.pop("ek_transfer", UNSET))

        def _parse_ek_restore(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_restore = _parse_ek_restore(d.pop("ek_restore", UNSET))

        def _parse_ek_soft_restore(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_soft_restore = _parse_ek_soft_restore(d.pop("ek_soft_restore", UNSET))

        def _parse_ek_setup(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_setup = _parse_ek_setup(d.pop("ek_setup", UNSET))

        def _parse_ek_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_update = _parse_ek_update(d.pop("ek_update", UNSET))

        def _parse_ek_trade(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_trade = _parse_ek_trade(d.pop("ek_trade", UNSET))

        def _parse_ek_domicile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ek_domicile = _parse_ek_domicile(d.pop("ek_domicile", UNSET))

        def _parse_vk_create(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vk_create = _parse_vk_create(d.pop("vk_create", UNSET))

        def _parse_vk_renew(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vk_renew = _parse_vk_renew(d.pop("vk_renew", UNSET))

        def _parse_vk_transfer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vk_transfer = _parse_vk_transfer(d.pop("vk_transfer", UNSET))

        def _parse_vk_domicile(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vk_domicile = _parse_vk_domicile(d.pop("vk_domicile", UNSET))

        prices_extra = d.pop("prices_extra", UNSET)

        def _parse_last_ek_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_ek_synced_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_ek_synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_ek_synced_at = _parse_last_ek_synced_at(d.pop("last_ek_synced_at", UNSET))

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

        registrar_tld_price_detail_request = cls(
            tld=tld,
            name=name,
            registrar_id=registrar_id,
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
            provider_status=provider_status,
            active=active,
            offerable=offerable,
            domicile_available=domicile_available,
            transfer_available=transfer_available,
            trade_available=trade_available,
            renew_available=renew_available,
            private_whois_allowed=private_whois_allowed,
            min_period=min_period,
            max_period=max_period,
            currency=currency,
            ek_create=ek_create,
            ek_renew=ek_renew,
            ek_transfer=ek_transfer,
            ek_restore=ek_restore,
            ek_soft_restore=ek_soft_restore,
            ek_setup=ek_setup,
            ek_update=ek_update,
            ek_trade=ek_trade,
            ek_domicile=ek_domicile,
            vk_create=vk_create,
            vk_renew=vk_renew,
            vk_transfer=vk_transfer,
            vk_domicile=vk_domicile,
            prices_extra=prices_extra,
            last_ek_synced_at=last_ek_synced_at,
            archived_by=archived_by,
            managed_by_content_type=managed_by_content_type,
            modified_by_user=modified_by_user,
            created_by_user=created_by_user,
        )

        registrar_tld_price_detail_request.additional_properties = d
        return registrar_tld_price_detail_request

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
