from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_annotations_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_archived_at_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_archived_by_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_archived_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_archived_reason_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_created_by_component_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_created_by_user_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_credential_id_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_criticality_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_debug_mode_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_default_ttl_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateDefaultTtlErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_display_name_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_algorithm_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateDnssecAlgorithmErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_cryptokeys_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateDnssecCryptokeysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_ds_records_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateDnssecDsRecordsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_enabled_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateDnssecEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_nsec_3_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateDnssecNsec3ErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_ds_delegation_synced_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateDsDelegationSyncedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_kind_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateKindErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_labels_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_managed_by_content_type_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_managed_by_object_id_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_modified_by_user_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_name_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateNameErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_non_field_errors_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_ns_delegation_synced_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateNsDelegationSyncedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_organization_id_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_platform_dns_record_created_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_platform_service_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_powerdns_metadata_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreatePowerdnsMetadataErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_primary_zone_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreatePrimaryZoneErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_provider_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateProviderErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_provider_id_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_provider_reference_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_reconciliation_enabled_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_sla_availability_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_sla_target_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_sla_window_days_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_slo_availability_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_slo_target_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_slo_window_days_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_sync_from_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateSyncFromErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_target_availability_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_disable_dnssec_create_tolerations_error_component import (
        ApiV1DomainsDnszonesDisableDnssecCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDnszonesDisableDnssecCreateValidationError")


@_attrs_define
class ApiV1DomainsDnszonesDisableDnssecCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDnszonesDisableDnssecCreateAnnotationsErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateArchivedAtErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateArchivedByErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateArchivedErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateArchivedReasonErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateCreatedByComponentErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateCreatedByUserErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateCredentialIdErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateCriticalityErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateDebugModeErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateDefaultTtlErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateDisplayNameErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecAlgorithmErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecCryptokeysErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecDsRecordsErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecEnabledErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecNsec3ErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateDsDelegationSyncedErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateKindErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateLabelsErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateManagedByContentTypeErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateManagedByObjectIdErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateModifiedByUserErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateNameErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateNonFieldErrorsErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateNsDelegationSyncedErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateOrganizationIdErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreatePlatformServiceErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreatePowerdnsMetadataErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreatePrimaryZoneErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateProviderErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateProviderIdErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateProviderReferenceErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateReconciliationEnabledErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateSlaAvailabilityErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateSlaTargetErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateSlaWindowDaysErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateSloAvailabilityErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateSloTargetErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateSloWindowDaysErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateSyncFromErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateTargetAvailabilityErrorComponent |
            ApiV1DomainsDnszonesDisableDnssecCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDnszonesDisableDnssecCreateAnnotationsErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateArchivedAtErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateArchivedByErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateArchivedErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateArchivedReasonErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateCreatedByComponentErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateCreatedByUserErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateCredentialIdErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateCriticalityErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateDebugModeErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateDefaultTtlErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateDisplayNameErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateDnssecAlgorithmErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateDnssecCryptokeysErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateDnssecDsRecordsErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateDnssecEnabledErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateDnssecNsec3ErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateDsDelegationSyncedErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateKindErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateLabelsErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateManagedByContentTypeErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateManagedByObjectIdErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateModifiedByUserErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateNameErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateNonFieldErrorsErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateNsDelegationSyncedErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateOrganizationIdErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreatePlatformServiceErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreatePowerdnsMetadataErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreatePrimaryZoneErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateProviderErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateProviderIdErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateProviderReferenceErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateReconciliationEnabledErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateSlaAvailabilityErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateSlaTargetErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateSlaWindowDaysErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateSloAvailabilityErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateSloTargetErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateSloWindowDaysErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateSyncFromErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateTargetAvailabilityErrorComponent
        | ApiV1DomainsDnszonesDisableDnssecCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_annotations_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_archived_at_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_archived_by_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_archived_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateArchivedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_archived_reason_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_created_by_component_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_created_by_user_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_credential_id_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateCredentialIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_criticality_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_debug_mode_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_default_ttl_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDefaultTtlErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_display_name_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_algorithm_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecAlgorithmErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_cryptokeys_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecCryptokeysErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_ds_records_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecDsRecordsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_enabled_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecEnabledErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_nsec_3_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecNsec3ErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_ds_delegation_synced_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDsDelegationSyncedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_kind_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateKindErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_labels_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateLabelsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_managed_by_content_type_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_managed_by_object_id_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_modified_by_user_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_name_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateNameErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_non_field_errors_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_ns_delegation_synced_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateNsDelegationSyncedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_organization_id_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_platform_service_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_powerdns_metadata_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreatePowerdnsMetadataErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_primary_zone_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreatePrimaryZoneErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_provider_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateProviderErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_provider_id_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_provider_reference_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_sla_availability_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_sla_target_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_sla_window_days_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_slo_availability_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_slo_target_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_slo_window_days_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_target_availability_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_tolerations_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreatePrimaryZoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreatePowerdnsMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateDefaultTtlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateDnssecEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateDnssecAlgorithmErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateDnssecNsec3ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateDnssecDsRecordsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateDnssecCryptokeysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateNsDelegationSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateDsDelegationSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateManagedByContentTypeErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesDisableDnssecCreateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_annotations_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_archived_at_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_archived_by_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_archived_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateArchivedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_archived_reason_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_created_by_component_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_created_by_user_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_credential_id_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateCredentialIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_criticality_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_debug_mode_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_default_ttl_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDefaultTtlErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_display_name_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_algorithm_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecAlgorithmErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_cryptokeys_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecCryptokeysErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_ds_records_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecDsRecordsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_enabled_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecEnabledErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_dnssec_nsec_3_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDnssecNsec3ErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_ds_delegation_synced_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateDsDelegationSyncedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_kind_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateKindErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_labels_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateLabelsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_managed_by_content_type_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_managed_by_object_id_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_modified_by_user_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_name_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateNameErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_non_field_errors_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_ns_delegation_synced_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateNsDelegationSyncedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_organization_id_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_platform_service_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_powerdns_metadata_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreatePowerdnsMetadataErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_primary_zone_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreatePrimaryZoneErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_provider_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateProviderErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_provider_id_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_provider_reference_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_sla_availability_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_sla_target_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_sla_window_days_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_slo_availability_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_slo_target_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_slo_window_days_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_sync_from_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateSyncFromErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_target_availability_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_disable_dnssec_create_tolerations_error_component import (
            ApiV1DomainsDnszonesDisableDnssecCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDnszonesDisableDnssecCreateAnnotationsErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateArchivedAtErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateArchivedByErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateArchivedErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateArchivedReasonErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateCreatedByComponentErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateCreatedByUserErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateCredentialIdErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateCriticalityErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateDebugModeErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateDefaultTtlErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateDisplayNameErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateDnssecAlgorithmErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateDnssecCryptokeysErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateDnssecDsRecordsErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateDnssecEnabledErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateDnssecNsec3ErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateDsDelegationSyncedErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateKindErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateLabelsErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateManagedByContentTypeErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateManagedByObjectIdErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateModifiedByUserErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateNameErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateNonFieldErrorsErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateNsDelegationSyncedErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateOrganizationIdErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreatePlatformServiceErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreatePowerdnsMetadataErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreatePrimaryZoneErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateProviderErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateProviderIdErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateProviderReferenceErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateReconciliationEnabledErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateSlaAvailabilityErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateSlaTargetErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateSlaWindowDaysErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateSloAvailabilityErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateSloTargetErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateSloWindowDaysErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateSyncFromErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateTargetAvailabilityErrorComponent
                | ApiV1DomainsDnszonesDisableDnssecCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_0 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_1 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_2 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_3 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_4 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_5 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_6 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_7 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_8 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_9 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_10 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_11 = ApiV1DomainsDnszonesDisableDnssecCreateLastReconciliationDurationSecondsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_12 = (
                        ApiV1DomainsDnszonesDisableDnssecCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_13 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_14 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_15 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_16 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_17 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_18 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_19 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_20 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_21 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_22 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_23 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_24 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_25 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_26 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_27 = (
                        ApiV1DomainsDnszonesDisableDnssecCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_28 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_29 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_30 = (
                        ApiV1DomainsDnszonesDisableDnssecCreatePrimaryZoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_31 = (
                        ApiV1DomainsDnszonesDisableDnssecCreatePowerdnsMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_32 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateDefaultTtlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_33 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateDnssecEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_34 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateDnssecAlgorithmErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_35 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateDnssecNsec3ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_36 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateDnssecDsRecordsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_37 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateDnssecCryptokeysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_38 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateNsDelegationSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_39 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateDsDelegationSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_40 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_41 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_42 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_43 = (
                        ApiV1DomainsDnszonesDisableDnssecCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_44 = (
                    ApiV1DomainsDnszonesDisableDnssecCreateSyncFromErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_dnszones_disable_dnssec_create_error_type_44

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_dnszones_disable_dnssec_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_dnszones_disable_dnssec_create_validation_error.additional_properties = d
        return api_v1_domains_dnszones_disable_dnssec_create_validation_error

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
