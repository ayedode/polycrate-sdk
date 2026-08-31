from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_dnszones_rectify_create_annotations_error_component import (
        ApiV1DomainsDnszonesRectifyCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_archived_at_error_component import (
        ApiV1DomainsDnszonesRectifyCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_archived_by_error_component import (
        ApiV1DomainsDnszonesRectifyCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_archived_error_component import (
        ApiV1DomainsDnszonesRectifyCreateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_archived_reason_error_component import (
        ApiV1DomainsDnszonesRectifyCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_created_by_component_error_component import (
        ApiV1DomainsDnszonesRectifyCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_created_by_user_error_component import (
        ApiV1DomainsDnszonesRectifyCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_credential_id_error_component import (
        ApiV1DomainsDnszonesRectifyCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_criticality_error_component import (
        ApiV1DomainsDnszonesRectifyCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_debug_mode_error_component import (
        ApiV1DomainsDnszonesRectifyCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_default_ttl_error_component import (
        ApiV1DomainsDnszonesRectifyCreateDefaultTtlErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_display_name_error_component import (
        ApiV1DomainsDnszonesRectifyCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_dnssec_algorithm_error_component import (
        ApiV1DomainsDnszonesRectifyCreateDnssecAlgorithmErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_dnssec_cryptokeys_error_component import (
        ApiV1DomainsDnszonesRectifyCreateDnssecCryptokeysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_dnssec_ds_records_error_component import (
        ApiV1DomainsDnszonesRectifyCreateDnssecDsRecordsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_dnssec_enabled_error_component import (
        ApiV1DomainsDnszonesRectifyCreateDnssecEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_dnssec_nsec_3_error_component import (
        ApiV1DomainsDnszonesRectifyCreateDnssecNsec3ErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_ds_delegation_synced_error_component import (
        ApiV1DomainsDnszonesRectifyCreateDsDelegationSyncedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_kind_error_component import (
        ApiV1DomainsDnszonesRectifyCreateKindErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_labels_error_component import (
        ApiV1DomainsDnszonesRectifyCreateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDnszonesRectifyCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_managed_by_content_type_error_component import (
        ApiV1DomainsDnszonesRectifyCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_managed_by_object_id_error_component import (
        ApiV1DomainsDnszonesRectifyCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_modified_by_user_error_component import (
        ApiV1DomainsDnszonesRectifyCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_name_error_component import (
        ApiV1DomainsDnszonesRectifyCreateNameErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_non_field_errors_error_component import (
        ApiV1DomainsDnszonesRectifyCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_ns_delegation_synced_error_component import (
        ApiV1DomainsDnszonesRectifyCreateNsDelegationSyncedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_organization_id_error_component import (
        ApiV1DomainsDnszonesRectifyCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_platform_dns_record_created_error_component import (
        ApiV1DomainsDnszonesRectifyCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_platform_service_error_component import (
        ApiV1DomainsDnszonesRectifyCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_powerdns_metadata_error_component import (
        ApiV1DomainsDnszonesRectifyCreatePowerdnsMetadataErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_primary_zone_error_component import (
        ApiV1DomainsDnszonesRectifyCreatePrimaryZoneErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_provider_error_component import (
        ApiV1DomainsDnszonesRectifyCreateProviderErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_provider_id_error_component import (
        ApiV1DomainsDnszonesRectifyCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_provider_reference_error_component import (
        ApiV1DomainsDnszonesRectifyCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_reconciliation_enabled_error_component import (
        ApiV1DomainsDnszonesRectifyCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_sla_availability_error_component import (
        ApiV1DomainsDnszonesRectifyCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_sla_target_error_component import (
        ApiV1DomainsDnszonesRectifyCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_sla_window_days_error_component import (
        ApiV1DomainsDnszonesRectifyCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_slo_availability_error_component import (
        ApiV1DomainsDnszonesRectifyCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_slo_target_error_component import (
        ApiV1DomainsDnszonesRectifyCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_slo_window_days_error_component import (
        ApiV1DomainsDnszonesRectifyCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_sync_from_error_component import (
        ApiV1DomainsDnszonesRectifyCreateSyncFromErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_target_availability_error_component import (
        ApiV1DomainsDnszonesRectifyCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_rectify_create_tolerations_error_component import (
        ApiV1DomainsDnszonesRectifyCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDnszonesRectifyCreateValidationError")


@_attrs_define
class ApiV1DomainsDnszonesRectifyCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDnszonesRectifyCreateAnnotationsErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateArchivedAtErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateArchivedByErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateArchivedErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateArchivedReasonErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateCreatedByComponentErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateCreatedByUserErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateCredentialIdErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateCriticalityErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateDebugModeErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateDefaultTtlErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateDisplayNameErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateDnssecAlgorithmErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateDnssecCryptokeysErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateDnssecDsRecordsErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateDnssecEnabledErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateDnssecNsec3ErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateDsDelegationSyncedErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateKindErrorComponent | ApiV1DomainsDnszonesRectifyCreateLabelsErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateManagedByContentTypeErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateManagedByObjectIdErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateModifiedByUserErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateNameErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateNonFieldErrorsErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateNsDelegationSyncedErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateOrganizationIdErrorComponent |
            ApiV1DomainsDnszonesRectifyCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDnszonesRectifyCreatePlatformServiceErrorComponent |
            ApiV1DomainsDnszonesRectifyCreatePowerdnsMetadataErrorComponent |
            ApiV1DomainsDnszonesRectifyCreatePrimaryZoneErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateProviderErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateProviderIdErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateProviderReferenceErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateReconciliationEnabledErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateSlaAvailabilityErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateSlaTargetErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateSlaWindowDaysErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateSloAvailabilityErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateSloTargetErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateSloWindowDaysErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateSyncFromErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateTargetAvailabilityErrorComponent |
            ApiV1DomainsDnszonesRectifyCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDnszonesRectifyCreateAnnotationsErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateArchivedAtErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateArchivedByErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateArchivedErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateArchivedReasonErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateCreatedByComponentErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateCreatedByUserErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateCredentialIdErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateCriticalityErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateDebugModeErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateDefaultTtlErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateDisplayNameErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateDnssecAlgorithmErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateDnssecCryptokeysErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateDnssecDsRecordsErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateDnssecEnabledErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateDnssecNsec3ErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateDsDelegationSyncedErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateKindErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateLabelsErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateManagedByContentTypeErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateManagedByObjectIdErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateModifiedByUserErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateNameErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateNonFieldErrorsErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateNsDelegationSyncedErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateOrganizationIdErrorComponent
        | ApiV1DomainsDnszonesRectifyCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDnszonesRectifyCreatePlatformServiceErrorComponent
        | ApiV1DomainsDnszonesRectifyCreatePowerdnsMetadataErrorComponent
        | ApiV1DomainsDnszonesRectifyCreatePrimaryZoneErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateProviderErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateProviderIdErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateProviderReferenceErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateReconciliationEnabledErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateSlaAvailabilityErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateSlaTargetErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateSlaWindowDaysErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateSloAvailabilityErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateSloTargetErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateSloWindowDaysErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateSyncFromErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateTargetAvailabilityErrorComponent
        | ApiV1DomainsDnszonesRectifyCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_dnszones_rectify_create_annotations_error_component import (
            ApiV1DomainsDnszonesRectifyCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_archived_at_error_component import (
            ApiV1DomainsDnszonesRectifyCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_archived_by_error_component import (
            ApiV1DomainsDnszonesRectifyCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_archived_error_component import (
            ApiV1DomainsDnszonesRectifyCreateArchivedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_archived_reason_error_component import (
            ApiV1DomainsDnszonesRectifyCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_created_by_component_error_component import (
            ApiV1DomainsDnszonesRectifyCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_created_by_user_error_component import (
            ApiV1DomainsDnszonesRectifyCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_credential_id_error_component import (
            ApiV1DomainsDnszonesRectifyCreateCredentialIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_criticality_error_component import (
            ApiV1DomainsDnszonesRectifyCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_debug_mode_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_default_ttl_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDefaultTtlErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_display_name_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_dnssec_algorithm_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDnssecAlgorithmErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_dnssec_cryptokeys_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDnssecCryptokeysErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_dnssec_ds_records_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDnssecDsRecordsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_dnssec_enabled_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDnssecEnabledErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_dnssec_nsec_3_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDnssecNsec3ErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_ds_delegation_synced_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDsDelegationSyncedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_kind_error_component import (
            ApiV1DomainsDnszonesRectifyCreateKindErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_labels_error_component import (
            ApiV1DomainsDnszonesRectifyCreateLabelsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnszonesRectifyCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_managed_by_content_type_error_component import (
            ApiV1DomainsDnszonesRectifyCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_managed_by_object_id_error_component import (
            ApiV1DomainsDnszonesRectifyCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_modified_by_user_error_component import (
            ApiV1DomainsDnszonesRectifyCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_name_error_component import (
            ApiV1DomainsDnszonesRectifyCreateNameErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_non_field_errors_error_component import (
            ApiV1DomainsDnszonesRectifyCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_ns_delegation_synced_error_component import (
            ApiV1DomainsDnszonesRectifyCreateNsDelegationSyncedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_organization_id_error_component import (
            ApiV1DomainsDnszonesRectifyCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDnszonesRectifyCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_platform_service_error_component import (
            ApiV1DomainsDnszonesRectifyCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_powerdns_metadata_error_component import (
            ApiV1DomainsDnszonesRectifyCreatePowerdnsMetadataErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_primary_zone_error_component import (
            ApiV1DomainsDnszonesRectifyCreatePrimaryZoneErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_provider_error_component import (
            ApiV1DomainsDnszonesRectifyCreateProviderErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_provider_id_error_component import (
            ApiV1DomainsDnszonesRectifyCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_provider_reference_error_component import (
            ApiV1DomainsDnszonesRectifyCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDnszonesRectifyCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_sla_availability_error_component import (
            ApiV1DomainsDnszonesRectifyCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_sla_target_error_component import (
            ApiV1DomainsDnszonesRectifyCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_sla_window_days_error_component import (
            ApiV1DomainsDnszonesRectifyCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_slo_availability_error_component import (
            ApiV1DomainsDnszonesRectifyCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_slo_target_error_component import (
            ApiV1DomainsDnszonesRectifyCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_slo_window_days_error_component import (
            ApiV1DomainsDnszonesRectifyCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_target_availability_error_component import (
            ApiV1DomainsDnszonesRectifyCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_tolerations_error_component import (
            ApiV1DomainsDnszonesRectifyCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnszonesRectifyCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreatePrimaryZoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreatePowerdnsMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateDefaultTtlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateDnssecEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateDnssecAlgorithmErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateDnssecNsec3ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateDnssecDsRecordsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateDnssecCryptokeysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateNsDelegationSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateDsDelegationSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesRectifyCreateCreatedByUserErrorComponent):
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
        from ..models.api_v1_domains_dnszones_rectify_create_annotations_error_component import (
            ApiV1DomainsDnszonesRectifyCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_archived_at_error_component import (
            ApiV1DomainsDnszonesRectifyCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_archived_by_error_component import (
            ApiV1DomainsDnszonesRectifyCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_archived_error_component import (
            ApiV1DomainsDnszonesRectifyCreateArchivedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_archived_reason_error_component import (
            ApiV1DomainsDnszonesRectifyCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_created_by_component_error_component import (
            ApiV1DomainsDnszonesRectifyCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_created_by_user_error_component import (
            ApiV1DomainsDnszonesRectifyCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_credential_id_error_component import (
            ApiV1DomainsDnszonesRectifyCreateCredentialIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_criticality_error_component import (
            ApiV1DomainsDnszonesRectifyCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_debug_mode_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_default_ttl_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDefaultTtlErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_display_name_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_dnssec_algorithm_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDnssecAlgorithmErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_dnssec_cryptokeys_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDnssecCryptokeysErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_dnssec_ds_records_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDnssecDsRecordsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_dnssec_enabled_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDnssecEnabledErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_dnssec_nsec_3_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDnssecNsec3ErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_ds_delegation_synced_error_component import (
            ApiV1DomainsDnszonesRectifyCreateDsDelegationSyncedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_kind_error_component import (
            ApiV1DomainsDnszonesRectifyCreateKindErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_labels_error_component import (
            ApiV1DomainsDnszonesRectifyCreateLabelsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnszonesRectifyCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_managed_by_content_type_error_component import (
            ApiV1DomainsDnszonesRectifyCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_managed_by_object_id_error_component import (
            ApiV1DomainsDnszonesRectifyCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_modified_by_user_error_component import (
            ApiV1DomainsDnszonesRectifyCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_name_error_component import (
            ApiV1DomainsDnszonesRectifyCreateNameErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_non_field_errors_error_component import (
            ApiV1DomainsDnszonesRectifyCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_ns_delegation_synced_error_component import (
            ApiV1DomainsDnszonesRectifyCreateNsDelegationSyncedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_organization_id_error_component import (
            ApiV1DomainsDnszonesRectifyCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDnszonesRectifyCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_platform_service_error_component import (
            ApiV1DomainsDnszonesRectifyCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_powerdns_metadata_error_component import (
            ApiV1DomainsDnszonesRectifyCreatePowerdnsMetadataErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_primary_zone_error_component import (
            ApiV1DomainsDnszonesRectifyCreatePrimaryZoneErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_provider_error_component import (
            ApiV1DomainsDnszonesRectifyCreateProviderErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_provider_id_error_component import (
            ApiV1DomainsDnszonesRectifyCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_provider_reference_error_component import (
            ApiV1DomainsDnszonesRectifyCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDnszonesRectifyCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_sla_availability_error_component import (
            ApiV1DomainsDnszonesRectifyCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_sla_target_error_component import (
            ApiV1DomainsDnszonesRectifyCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_sla_window_days_error_component import (
            ApiV1DomainsDnszonesRectifyCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_slo_availability_error_component import (
            ApiV1DomainsDnszonesRectifyCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_slo_target_error_component import (
            ApiV1DomainsDnszonesRectifyCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_slo_window_days_error_component import (
            ApiV1DomainsDnszonesRectifyCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_sync_from_error_component import (
            ApiV1DomainsDnszonesRectifyCreateSyncFromErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_target_availability_error_component import (
            ApiV1DomainsDnszonesRectifyCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_dnszones_rectify_create_tolerations_error_component import (
            ApiV1DomainsDnszonesRectifyCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDnszonesRectifyCreateAnnotationsErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateArchivedAtErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateArchivedByErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateArchivedErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateArchivedReasonErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateCreatedByComponentErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateCreatedByUserErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateCredentialIdErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateCriticalityErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateDebugModeErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateDefaultTtlErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateDisplayNameErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateDnssecAlgorithmErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateDnssecCryptokeysErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateDnssecDsRecordsErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateDnssecEnabledErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateDnssecNsec3ErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateDsDelegationSyncedErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateKindErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateLabelsErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateManagedByContentTypeErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateManagedByObjectIdErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateModifiedByUserErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateNameErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateNonFieldErrorsErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateNsDelegationSyncedErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateOrganizationIdErrorComponent
                | ApiV1DomainsDnszonesRectifyCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDnszonesRectifyCreatePlatformServiceErrorComponent
                | ApiV1DomainsDnszonesRectifyCreatePowerdnsMetadataErrorComponent
                | ApiV1DomainsDnszonesRectifyCreatePrimaryZoneErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateProviderErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateProviderIdErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateProviderReferenceErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateReconciliationEnabledErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateSlaAvailabilityErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateSlaTargetErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateSlaWindowDaysErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateSloAvailabilityErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateSloTargetErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateSloWindowDaysErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateSyncFromErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateTargetAvailabilityErrorComponent
                | ApiV1DomainsDnszonesRectifyCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_0 = (
                        ApiV1DomainsDnszonesRectifyCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_1 = (
                        ApiV1DomainsDnszonesRectifyCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_2 = (
                        ApiV1DomainsDnszonesRectifyCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_3 = (
                        ApiV1DomainsDnszonesRectifyCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_4 = (
                        ApiV1DomainsDnszonesRectifyCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_5 = (
                        ApiV1DomainsDnszonesRectifyCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_6 = (
                        ApiV1DomainsDnszonesRectifyCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_7 = (
                        ApiV1DomainsDnszonesRectifyCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_8 = (
                        ApiV1DomainsDnszonesRectifyCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_9 = (
                        ApiV1DomainsDnszonesRectifyCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_10 = (
                        ApiV1DomainsDnszonesRectifyCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_11 = (
                        ApiV1DomainsDnszonesRectifyCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_12 = (
                        ApiV1DomainsDnszonesRectifyCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_13 = (
                        ApiV1DomainsDnszonesRectifyCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_14 = (
                        ApiV1DomainsDnszonesRectifyCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_15 = (
                        ApiV1DomainsDnszonesRectifyCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_16 = (
                        ApiV1DomainsDnszonesRectifyCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_17 = (
                        ApiV1DomainsDnszonesRectifyCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_18 = (
                        ApiV1DomainsDnszonesRectifyCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_19 = (
                        ApiV1DomainsDnszonesRectifyCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_20 = (
                        ApiV1DomainsDnszonesRectifyCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_21 = (
                        ApiV1DomainsDnszonesRectifyCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_22 = (
                        ApiV1DomainsDnszonesRectifyCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_23 = (
                        ApiV1DomainsDnszonesRectifyCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_24 = (
                        ApiV1DomainsDnszonesRectifyCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_25 = (
                        ApiV1DomainsDnszonesRectifyCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_26 = (
                        ApiV1DomainsDnszonesRectifyCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_27 = (
                        ApiV1DomainsDnszonesRectifyCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_28 = (
                        ApiV1DomainsDnszonesRectifyCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_29 = (
                        ApiV1DomainsDnszonesRectifyCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_30 = (
                        ApiV1DomainsDnszonesRectifyCreatePrimaryZoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_31 = (
                        ApiV1DomainsDnszonesRectifyCreatePowerdnsMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_32 = (
                        ApiV1DomainsDnszonesRectifyCreateDefaultTtlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_33 = (
                        ApiV1DomainsDnszonesRectifyCreateDnssecEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_34 = (
                        ApiV1DomainsDnszonesRectifyCreateDnssecAlgorithmErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_35 = (
                        ApiV1DomainsDnszonesRectifyCreateDnssecNsec3ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_36 = (
                        ApiV1DomainsDnszonesRectifyCreateDnssecDsRecordsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_37 = (
                        ApiV1DomainsDnszonesRectifyCreateDnssecCryptokeysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_38 = (
                        ApiV1DomainsDnszonesRectifyCreateNsDelegationSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_39 = (
                        ApiV1DomainsDnszonesRectifyCreateDsDelegationSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_40 = (
                        ApiV1DomainsDnszonesRectifyCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_41 = (
                        ApiV1DomainsDnszonesRectifyCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_42 = (
                        ApiV1DomainsDnszonesRectifyCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_43 = (
                        ApiV1DomainsDnszonesRectifyCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_44 = (
                    ApiV1DomainsDnszonesRectifyCreateSyncFromErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_dnszones_rectify_create_error_type_44

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_dnszones_rectify_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_dnszones_rectify_create_validation_error.additional_properties = d
        return api_v1_domains_dnszones_rectify_create_validation_error

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
