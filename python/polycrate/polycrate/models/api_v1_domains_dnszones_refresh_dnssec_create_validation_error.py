from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_annotations_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_archived_at_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_archived_by_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_archived_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_archived_reason_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_created_by_component_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_created_by_user_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_credential_id_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_criticality_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_debug_mode_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_default_ttl_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateDefaultTtlErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_display_name_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_algorithm_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateDnssecAlgorithmErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_cryptokeys_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateDnssecCryptokeysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_ds_records_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateDnssecDsRecordsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_enabled_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateDnssecEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_nsec_3_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateDnssecNsec3ErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_ds_delegation_synced_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateDsDelegationSyncedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_kind_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateKindErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_labels_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_managed_by_content_type_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_managed_by_object_id_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_modified_by_user_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_name_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateNameErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_non_field_errors_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_ns_delegation_synced_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateNsDelegationSyncedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_organization_id_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_platform_dns_record_created_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_platform_service_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_powerdns_metadata_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreatePowerdnsMetadataErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_primary_zone_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreatePrimaryZoneErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_provider_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateProviderErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_provider_id_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_provider_reference_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_reconciliation_enabled_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_sla_availability_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_sla_target_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_sla_window_days_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_slo_availability_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_slo_target_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_slo_window_days_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_sync_from_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateSyncFromErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_target_availability_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_refresh_dnssec_create_tolerations_error_component import (
        ApiV1DomainsDnszonesRefreshDnssecCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDnszonesRefreshDnssecCreateValidationError")


@_attrs_define
class ApiV1DomainsDnszonesRefreshDnssecCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDnszonesRefreshDnssecCreateAnnotationsErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateArchivedAtErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateArchivedByErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateArchivedErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateArchivedReasonErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByComponentErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByUserErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateCredentialIdErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateCriticalityErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateDebugModeErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateDefaultTtlErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateDisplayNameErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecAlgorithmErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecCryptokeysErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecDsRecordsErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecEnabledErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecNsec3ErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateDsDelegationSyncedErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateKindErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateLabelsErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateManagedByContentTypeErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateManagedByObjectIdErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateModifiedByUserErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateNameErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateNonFieldErrorsErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateNsDelegationSyncedErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateOrganizationIdErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreatePlatformServiceErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreatePowerdnsMetadataErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreatePrimaryZoneErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateProviderErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateProviderIdErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateProviderReferenceErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateReconciliationEnabledErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateSlaAvailabilityErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateSlaTargetErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateSlaWindowDaysErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateSloAvailabilityErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateSloTargetErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateSloWindowDaysErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateSyncFromErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateTargetAvailabilityErrorComponent |
            ApiV1DomainsDnszonesRefreshDnssecCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDnszonesRefreshDnssecCreateAnnotationsErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateArchivedAtErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateArchivedByErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateArchivedErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateArchivedReasonErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByComponentErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByUserErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateCredentialIdErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateCriticalityErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateDebugModeErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateDefaultTtlErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateDisplayNameErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateDnssecAlgorithmErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateDnssecCryptokeysErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateDnssecDsRecordsErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateDnssecEnabledErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateDnssecNsec3ErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateDsDelegationSyncedErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateKindErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateLabelsErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateManagedByContentTypeErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateManagedByObjectIdErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateModifiedByUserErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateNameErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateNonFieldErrorsErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateNsDelegationSyncedErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateOrganizationIdErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreatePlatformServiceErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreatePowerdnsMetadataErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreatePrimaryZoneErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateProviderErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateProviderIdErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateProviderReferenceErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateReconciliationEnabledErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateSlaAvailabilityErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateSlaTargetErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateSlaWindowDaysErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateSloAvailabilityErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateSloTargetErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateSloWindowDaysErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateSyncFromErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateTargetAvailabilityErrorComponent
        | ApiV1DomainsDnszonesRefreshDnssecCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_annotations_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_archived_at_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_archived_by_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_archived_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_archived_reason_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_created_by_component_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_created_by_user_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_credential_id_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_criticality_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_debug_mode_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_default_ttl_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDefaultTtlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_display_name_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_algorithm_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecAlgorithmErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_cryptokeys_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecCryptokeysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_ds_records_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecDsRecordsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_enabled_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_nsec_3_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecNsec3ErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_ds_delegation_synced_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_kind_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_labels_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_managed_by_content_type_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_managed_by_object_id_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_modified_by_user_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_name_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_non_field_errors_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_ns_delegation_synced_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateNsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_organization_id_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_platform_service_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_powerdns_metadata_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreatePowerdnsMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_primary_zone_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreatePrimaryZoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_provider_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_provider_id_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_provider_reference_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_sla_availability_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_sla_target_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_sla_window_days_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_slo_availability_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_slo_target_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_slo_window_days_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_target_availability_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_tolerations_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreatePlatformDnsRecordCreatedErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreatePrimaryZoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreatePowerdnsMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateDefaultTtlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateDnssecEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateDnssecAlgorithmErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateDnssecNsec3ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateDnssecDsRecordsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateDnssecCryptokeysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateNsDelegationSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateDsDelegationSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateManagedByContentTypeErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByUserErrorComponent):
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
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_annotations_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_archived_at_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_archived_by_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_archived_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_archived_reason_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_created_by_component_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_created_by_user_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_credential_id_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_criticality_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_debug_mode_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_default_ttl_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDefaultTtlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_display_name_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_algorithm_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecAlgorithmErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_cryptokeys_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecCryptokeysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_ds_records_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecDsRecordsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_enabled_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_dnssec_nsec_3_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDnssecNsec3ErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_ds_delegation_synced_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateDsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_kind_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_labels_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_managed_by_content_type_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_managed_by_object_id_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_modified_by_user_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_name_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_non_field_errors_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_ns_delegation_synced_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateNsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_organization_id_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_platform_service_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_powerdns_metadata_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreatePowerdnsMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_primary_zone_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreatePrimaryZoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_provider_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_provider_id_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_provider_reference_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_sla_availability_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_sla_target_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_sla_window_days_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_slo_availability_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_slo_target_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_slo_window_days_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_sync_from_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateSyncFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_target_availability_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_refresh_dnssec_create_tolerations_error_component import (
            ApiV1DomainsDnszonesRefreshDnssecCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDnszonesRefreshDnssecCreateAnnotationsErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateArchivedAtErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateArchivedByErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateArchivedErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateArchivedReasonErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByComponentErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByUserErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateCredentialIdErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateCriticalityErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateDebugModeErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateDefaultTtlErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateDisplayNameErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateDnssecAlgorithmErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateDnssecCryptokeysErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateDnssecDsRecordsErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateDnssecEnabledErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateDnssecNsec3ErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateDsDelegationSyncedErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateKindErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateLabelsErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateManagedByContentTypeErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateManagedByObjectIdErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateModifiedByUserErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateNameErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateNonFieldErrorsErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateNsDelegationSyncedErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateOrganizationIdErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreatePlatformServiceErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreatePowerdnsMetadataErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreatePrimaryZoneErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateProviderErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateProviderIdErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateProviderReferenceErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateReconciliationEnabledErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateSlaAvailabilityErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateSlaTargetErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateSlaWindowDaysErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateSloAvailabilityErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateSloTargetErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateSloWindowDaysErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateSyncFromErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateTargetAvailabilityErrorComponent
                | ApiV1DomainsDnszonesRefreshDnssecCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_0 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_1 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_2 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_3 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_4 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_5 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_6 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_7 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_8 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_9 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_10 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_11 = ApiV1DomainsDnszonesRefreshDnssecCreateLastReconciliationDurationSecondsErrorComponent.from_dict(
                        data
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_12 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_13 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_14 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_15 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_16 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_17 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_18 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_19 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_20 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_21 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_22 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_23 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_24 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_25 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_26 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_27 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_28 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_29 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_30 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreatePrimaryZoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_31 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreatePowerdnsMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_32 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateDefaultTtlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_33 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateDnssecEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_34 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateDnssecAlgorithmErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_35 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateDnssecNsec3ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_36 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateDnssecDsRecordsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_37 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateDnssecCryptokeysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_38 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateNsDelegationSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_39 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateDsDelegationSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_40 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_41 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_42 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_43 = (
                        ApiV1DomainsDnszonesRefreshDnssecCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_44 = (
                    ApiV1DomainsDnszonesRefreshDnssecCreateSyncFromErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_dnszones_refresh_dnssec_create_error_type_44

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_dnszones_refresh_dnssec_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_dnszones_refresh_dnssec_create_validation_error.additional_properties = d
        return api_v1_domains_dnszones_refresh_dnssec_create_validation_error

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
