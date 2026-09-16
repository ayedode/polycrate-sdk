from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_dnszones_create_annotations_error_component import (
        ApiV1DomainsDnszonesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_archived_at_error_component import (
        ApiV1DomainsDnszonesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_archived_by_error_component import (
        ApiV1DomainsDnszonesCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_archived_error_component import (
        ApiV1DomainsDnszonesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_archived_reason_error_component import (
        ApiV1DomainsDnszonesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_created_by_component_error_component import (
        ApiV1DomainsDnszonesCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_created_by_user_error_component import (
        ApiV1DomainsDnszonesCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_credential_id_error_component import (
        ApiV1DomainsDnszonesCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_criticality_error_component import (
        ApiV1DomainsDnszonesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_debug_mode_error_component import (
        ApiV1DomainsDnszonesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_default_ttl_error_component import (
        ApiV1DomainsDnszonesCreateDefaultTtlErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_display_name_error_component import (
        ApiV1DomainsDnszonesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_dnssec_algorithm_error_component import (
        ApiV1DomainsDnszonesCreateDnssecAlgorithmErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_dnssec_cryptokeys_error_component import (
        ApiV1DomainsDnszonesCreateDnssecCryptokeysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_dnssec_ds_records_error_component import (
        ApiV1DomainsDnszonesCreateDnssecDsRecordsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_dnssec_enabled_error_component import (
        ApiV1DomainsDnszonesCreateDnssecEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_dnssec_nsec_3_error_component import (
        ApiV1DomainsDnszonesCreateDnssecNsec3ErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_ds_delegation_synced_error_component import (
        ApiV1DomainsDnszonesCreateDsDelegationSyncedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_kind_error_component import (
        ApiV1DomainsDnszonesCreateKindErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_labels_error_component import (
        ApiV1DomainsDnszonesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDnszonesCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_managed_by_content_type_error_component import (
        ApiV1DomainsDnszonesCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_managed_by_object_id_error_component import (
        ApiV1DomainsDnszonesCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_modified_by_user_error_component import (
        ApiV1DomainsDnszonesCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_name_error_component import (
        ApiV1DomainsDnszonesCreateNameErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_non_field_errors_error_component import (
        ApiV1DomainsDnszonesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_ns_delegation_synced_error_component import (
        ApiV1DomainsDnszonesCreateNsDelegationSyncedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_organization_id_error_component import (
        ApiV1DomainsDnszonesCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_platform_dns_record_created_error_component import (
        ApiV1DomainsDnszonesCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_platform_service_error_component import (
        ApiV1DomainsDnszonesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_powerdns_metadata_error_component import (
        ApiV1DomainsDnszonesCreatePowerdnsMetadataErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_primary_zone_error_component import (
        ApiV1DomainsDnszonesCreatePrimaryZoneErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_provider_error_component import (
        ApiV1DomainsDnszonesCreateProviderErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_provider_id_error_component import (
        ApiV1DomainsDnszonesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_provider_reference_error_component import (
        ApiV1DomainsDnszonesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_reconciliation_enabled_error_component import (
        ApiV1DomainsDnszonesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_sla_availability_error_component import (
        ApiV1DomainsDnszonesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_sla_target_error_component import (
        ApiV1DomainsDnszonesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_sla_window_days_error_component import (
        ApiV1DomainsDnszonesCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_slo_availability_error_component import (
        ApiV1DomainsDnszonesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_slo_target_error_component import (
        ApiV1DomainsDnszonesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_slo_window_days_error_component import (
        ApiV1DomainsDnszonesCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_sync_from_error_component import (
        ApiV1DomainsDnszonesCreateSyncFromErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_target_availability_error_component import (
        ApiV1DomainsDnszonesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_dnszones_create_tolerations_error_component import (
        ApiV1DomainsDnszonesCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDnszonesCreateValidationError")


@_attrs_define
class ApiV1DomainsDnszonesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDnszonesCreateAnnotationsErrorComponent |
            ApiV1DomainsDnszonesCreateArchivedAtErrorComponent | ApiV1DomainsDnszonesCreateArchivedByErrorComponent |
            ApiV1DomainsDnszonesCreateArchivedErrorComponent | ApiV1DomainsDnszonesCreateArchivedReasonErrorComponent |
            ApiV1DomainsDnszonesCreateCreatedByComponentErrorComponent |
            ApiV1DomainsDnszonesCreateCreatedByUserErrorComponent | ApiV1DomainsDnszonesCreateCredentialIdErrorComponent |
            ApiV1DomainsDnszonesCreateCriticalityErrorComponent | ApiV1DomainsDnszonesCreateDebugModeErrorComponent |
            ApiV1DomainsDnszonesCreateDefaultTtlErrorComponent | ApiV1DomainsDnszonesCreateDisplayNameErrorComponent |
            ApiV1DomainsDnszonesCreateDnssecAlgorithmErrorComponent |
            ApiV1DomainsDnszonesCreateDnssecCryptokeysErrorComponent |
            ApiV1DomainsDnszonesCreateDnssecDsRecordsErrorComponent | ApiV1DomainsDnszonesCreateDnssecEnabledErrorComponent
            | ApiV1DomainsDnszonesCreateDnssecNsec3ErrorComponent |
            ApiV1DomainsDnszonesCreateDsDelegationSyncedErrorComponent | ApiV1DomainsDnszonesCreateKindErrorComponent |
            ApiV1DomainsDnszonesCreateLabelsErrorComponent |
            ApiV1DomainsDnszonesCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDnszonesCreateManagedByContentTypeErrorComponent |
            ApiV1DomainsDnszonesCreateManagedByObjectIdErrorComponent |
            ApiV1DomainsDnszonesCreateModifiedByUserErrorComponent | ApiV1DomainsDnszonesCreateNameErrorComponent |
            ApiV1DomainsDnszonesCreateNonFieldErrorsErrorComponent |
            ApiV1DomainsDnszonesCreateNsDelegationSyncedErrorComponent |
            ApiV1DomainsDnszonesCreateOrganizationIdErrorComponent |
            ApiV1DomainsDnszonesCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDnszonesCreatePlatformServiceErrorComponent |
            ApiV1DomainsDnszonesCreatePowerdnsMetadataErrorComponent | ApiV1DomainsDnszonesCreatePrimaryZoneErrorComponent |
            ApiV1DomainsDnszonesCreateProviderErrorComponent | ApiV1DomainsDnszonesCreateProviderIdErrorComponent |
            ApiV1DomainsDnszonesCreateProviderReferenceErrorComponent |
            ApiV1DomainsDnszonesCreateReconciliationEnabledErrorComponent |
            ApiV1DomainsDnszonesCreateSlaAvailabilityErrorComponent | ApiV1DomainsDnszonesCreateSlaTargetErrorComponent |
            ApiV1DomainsDnszonesCreateSlaWindowDaysErrorComponent | ApiV1DomainsDnszonesCreateSloAvailabilityErrorComponent
            | ApiV1DomainsDnszonesCreateSloTargetErrorComponent | ApiV1DomainsDnszonesCreateSloWindowDaysErrorComponent |
            ApiV1DomainsDnszonesCreateSyncFromErrorComponent | ApiV1DomainsDnszonesCreateTargetAvailabilityErrorComponent |
            ApiV1DomainsDnszonesCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDnszonesCreateAnnotationsErrorComponent
        | ApiV1DomainsDnszonesCreateArchivedAtErrorComponent
        | ApiV1DomainsDnszonesCreateArchivedByErrorComponent
        | ApiV1DomainsDnszonesCreateArchivedErrorComponent
        | ApiV1DomainsDnszonesCreateArchivedReasonErrorComponent
        | ApiV1DomainsDnszonesCreateCreatedByComponentErrorComponent
        | ApiV1DomainsDnszonesCreateCreatedByUserErrorComponent
        | ApiV1DomainsDnszonesCreateCredentialIdErrorComponent
        | ApiV1DomainsDnszonesCreateCriticalityErrorComponent
        | ApiV1DomainsDnszonesCreateDebugModeErrorComponent
        | ApiV1DomainsDnszonesCreateDefaultTtlErrorComponent
        | ApiV1DomainsDnszonesCreateDisplayNameErrorComponent
        | ApiV1DomainsDnszonesCreateDnssecAlgorithmErrorComponent
        | ApiV1DomainsDnszonesCreateDnssecCryptokeysErrorComponent
        | ApiV1DomainsDnszonesCreateDnssecDsRecordsErrorComponent
        | ApiV1DomainsDnszonesCreateDnssecEnabledErrorComponent
        | ApiV1DomainsDnszonesCreateDnssecNsec3ErrorComponent
        | ApiV1DomainsDnszonesCreateDsDelegationSyncedErrorComponent
        | ApiV1DomainsDnszonesCreateKindErrorComponent
        | ApiV1DomainsDnszonesCreateLabelsErrorComponent
        | ApiV1DomainsDnszonesCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDnszonesCreateManagedByContentTypeErrorComponent
        | ApiV1DomainsDnszonesCreateManagedByObjectIdErrorComponent
        | ApiV1DomainsDnszonesCreateModifiedByUserErrorComponent
        | ApiV1DomainsDnszonesCreateNameErrorComponent
        | ApiV1DomainsDnszonesCreateNonFieldErrorsErrorComponent
        | ApiV1DomainsDnszonesCreateNsDelegationSyncedErrorComponent
        | ApiV1DomainsDnszonesCreateOrganizationIdErrorComponent
        | ApiV1DomainsDnszonesCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDnszonesCreatePlatformServiceErrorComponent
        | ApiV1DomainsDnszonesCreatePowerdnsMetadataErrorComponent
        | ApiV1DomainsDnszonesCreatePrimaryZoneErrorComponent
        | ApiV1DomainsDnszonesCreateProviderErrorComponent
        | ApiV1DomainsDnszonesCreateProviderIdErrorComponent
        | ApiV1DomainsDnszonesCreateProviderReferenceErrorComponent
        | ApiV1DomainsDnszonesCreateReconciliationEnabledErrorComponent
        | ApiV1DomainsDnszonesCreateSlaAvailabilityErrorComponent
        | ApiV1DomainsDnszonesCreateSlaTargetErrorComponent
        | ApiV1DomainsDnszonesCreateSlaWindowDaysErrorComponent
        | ApiV1DomainsDnszonesCreateSloAvailabilityErrorComponent
        | ApiV1DomainsDnszonesCreateSloTargetErrorComponent
        | ApiV1DomainsDnszonesCreateSloWindowDaysErrorComponent
        | ApiV1DomainsDnszonesCreateSyncFromErrorComponent
        | ApiV1DomainsDnszonesCreateTargetAvailabilityErrorComponent
        | ApiV1DomainsDnszonesCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_dnszones_create_annotations_error_component import (
            ApiV1DomainsDnszonesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_archived_at_error_component import (
            ApiV1DomainsDnszonesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_archived_by_error_component import (
            ApiV1DomainsDnszonesCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_archived_error_component import (
            ApiV1DomainsDnszonesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_archived_reason_error_component import (
            ApiV1DomainsDnszonesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_created_by_component_error_component import (
            ApiV1DomainsDnszonesCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_created_by_user_error_component import (
            ApiV1DomainsDnszonesCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_credential_id_error_component import (
            ApiV1DomainsDnszonesCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_criticality_error_component import (
            ApiV1DomainsDnszonesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_debug_mode_error_component import (
            ApiV1DomainsDnszonesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_default_ttl_error_component import (
            ApiV1DomainsDnszonesCreateDefaultTtlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_display_name_error_component import (
            ApiV1DomainsDnszonesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_dnssec_algorithm_error_component import (
            ApiV1DomainsDnszonesCreateDnssecAlgorithmErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_dnssec_cryptokeys_error_component import (
            ApiV1DomainsDnszonesCreateDnssecCryptokeysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_dnssec_ds_records_error_component import (
            ApiV1DomainsDnszonesCreateDnssecDsRecordsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_dnssec_enabled_error_component import (
            ApiV1DomainsDnszonesCreateDnssecEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_dnssec_nsec_3_error_component import (
            ApiV1DomainsDnszonesCreateDnssecNsec3ErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_ds_delegation_synced_error_component import (
            ApiV1DomainsDnszonesCreateDsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_kind_error_component import (
            ApiV1DomainsDnszonesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_labels_error_component import (
            ApiV1DomainsDnszonesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnszonesCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_managed_by_content_type_error_component import (
            ApiV1DomainsDnszonesCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_managed_by_object_id_error_component import (
            ApiV1DomainsDnszonesCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_modified_by_user_error_component import (
            ApiV1DomainsDnszonesCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_name_error_component import (
            ApiV1DomainsDnszonesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_non_field_errors_error_component import (
            ApiV1DomainsDnszonesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_ns_delegation_synced_error_component import (
            ApiV1DomainsDnszonesCreateNsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_organization_id_error_component import (
            ApiV1DomainsDnszonesCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDnszonesCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_platform_service_error_component import (
            ApiV1DomainsDnszonesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_powerdns_metadata_error_component import (
            ApiV1DomainsDnszonesCreatePowerdnsMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_primary_zone_error_component import (
            ApiV1DomainsDnszonesCreatePrimaryZoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_provider_error_component import (
            ApiV1DomainsDnszonesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_provider_id_error_component import (
            ApiV1DomainsDnszonesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_provider_reference_error_component import (
            ApiV1DomainsDnszonesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDnszonesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_sla_availability_error_component import (
            ApiV1DomainsDnszonesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_sla_target_error_component import (
            ApiV1DomainsDnszonesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_sla_window_days_error_component import (
            ApiV1DomainsDnszonesCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_slo_availability_error_component import (
            ApiV1DomainsDnszonesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_slo_target_error_component import (
            ApiV1DomainsDnszonesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_slo_window_days_error_component import (
            ApiV1DomainsDnszonesCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_target_availability_error_component import (
            ApiV1DomainsDnszonesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_tolerations_error_component import (
            ApiV1DomainsDnszonesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDnszonesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDnszonesCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreatePrimaryZoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreatePowerdnsMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateDefaultTtlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateDnssecEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateDnssecAlgorithmErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateDnssecNsec3ErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateDnssecDsRecordsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateDnssecCryptokeysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateNsDelegationSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateDsDelegationSyncedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDnszonesCreateCreatedByUserErrorComponent):
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
        from ..models.api_v1_domains_dnszones_create_annotations_error_component import (
            ApiV1DomainsDnszonesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_archived_at_error_component import (
            ApiV1DomainsDnszonesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_archived_by_error_component import (
            ApiV1DomainsDnszonesCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_archived_error_component import (
            ApiV1DomainsDnszonesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_archived_reason_error_component import (
            ApiV1DomainsDnszonesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_created_by_component_error_component import (
            ApiV1DomainsDnszonesCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_created_by_user_error_component import (
            ApiV1DomainsDnszonesCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_credential_id_error_component import (
            ApiV1DomainsDnszonesCreateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_criticality_error_component import (
            ApiV1DomainsDnszonesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_debug_mode_error_component import (
            ApiV1DomainsDnszonesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_default_ttl_error_component import (
            ApiV1DomainsDnszonesCreateDefaultTtlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_display_name_error_component import (
            ApiV1DomainsDnszonesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_dnssec_algorithm_error_component import (
            ApiV1DomainsDnszonesCreateDnssecAlgorithmErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_dnssec_cryptokeys_error_component import (
            ApiV1DomainsDnszonesCreateDnssecCryptokeysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_dnssec_ds_records_error_component import (
            ApiV1DomainsDnszonesCreateDnssecDsRecordsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_dnssec_enabled_error_component import (
            ApiV1DomainsDnszonesCreateDnssecEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_dnssec_nsec_3_error_component import (
            ApiV1DomainsDnszonesCreateDnssecNsec3ErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_ds_delegation_synced_error_component import (
            ApiV1DomainsDnszonesCreateDsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_kind_error_component import (
            ApiV1DomainsDnszonesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_labels_error_component import (
            ApiV1DomainsDnszonesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDnszonesCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_managed_by_content_type_error_component import (
            ApiV1DomainsDnszonesCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_managed_by_object_id_error_component import (
            ApiV1DomainsDnszonesCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_modified_by_user_error_component import (
            ApiV1DomainsDnszonesCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_name_error_component import (
            ApiV1DomainsDnszonesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_non_field_errors_error_component import (
            ApiV1DomainsDnszonesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_ns_delegation_synced_error_component import (
            ApiV1DomainsDnszonesCreateNsDelegationSyncedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_organization_id_error_component import (
            ApiV1DomainsDnszonesCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDnszonesCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_platform_service_error_component import (
            ApiV1DomainsDnszonesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_powerdns_metadata_error_component import (
            ApiV1DomainsDnszonesCreatePowerdnsMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_primary_zone_error_component import (
            ApiV1DomainsDnszonesCreatePrimaryZoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_provider_error_component import (
            ApiV1DomainsDnszonesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_provider_id_error_component import (
            ApiV1DomainsDnszonesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_provider_reference_error_component import (
            ApiV1DomainsDnszonesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDnszonesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_sla_availability_error_component import (
            ApiV1DomainsDnszonesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_sla_target_error_component import (
            ApiV1DomainsDnszonesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_sla_window_days_error_component import (
            ApiV1DomainsDnszonesCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_slo_availability_error_component import (
            ApiV1DomainsDnszonesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_slo_target_error_component import (
            ApiV1DomainsDnszonesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_slo_window_days_error_component import (
            ApiV1DomainsDnszonesCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_sync_from_error_component import (
            ApiV1DomainsDnszonesCreateSyncFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_target_availability_error_component import (
            ApiV1DomainsDnszonesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_dnszones_create_tolerations_error_component import (
            ApiV1DomainsDnszonesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDnszonesCreateAnnotationsErrorComponent
                | ApiV1DomainsDnszonesCreateArchivedAtErrorComponent
                | ApiV1DomainsDnszonesCreateArchivedByErrorComponent
                | ApiV1DomainsDnszonesCreateArchivedErrorComponent
                | ApiV1DomainsDnszonesCreateArchivedReasonErrorComponent
                | ApiV1DomainsDnszonesCreateCreatedByComponentErrorComponent
                | ApiV1DomainsDnszonesCreateCreatedByUserErrorComponent
                | ApiV1DomainsDnszonesCreateCredentialIdErrorComponent
                | ApiV1DomainsDnszonesCreateCriticalityErrorComponent
                | ApiV1DomainsDnszonesCreateDebugModeErrorComponent
                | ApiV1DomainsDnszonesCreateDefaultTtlErrorComponent
                | ApiV1DomainsDnszonesCreateDisplayNameErrorComponent
                | ApiV1DomainsDnszonesCreateDnssecAlgorithmErrorComponent
                | ApiV1DomainsDnszonesCreateDnssecCryptokeysErrorComponent
                | ApiV1DomainsDnszonesCreateDnssecDsRecordsErrorComponent
                | ApiV1DomainsDnszonesCreateDnssecEnabledErrorComponent
                | ApiV1DomainsDnszonesCreateDnssecNsec3ErrorComponent
                | ApiV1DomainsDnszonesCreateDsDelegationSyncedErrorComponent
                | ApiV1DomainsDnszonesCreateKindErrorComponent
                | ApiV1DomainsDnszonesCreateLabelsErrorComponent
                | ApiV1DomainsDnszonesCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDnszonesCreateManagedByContentTypeErrorComponent
                | ApiV1DomainsDnszonesCreateManagedByObjectIdErrorComponent
                | ApiV1DomainsDnszonesCreateModifiedByUserErrorComponent
                | ApiV1DomainsDnszonesCreateNameErrorComponent
                | ApiV1DomainsDnszonesCreateNonFieldErrorsErrorComponent
                | ApiV1DomainsDnszonesCreateNsDelegationSyncedErrorComponent
                | ApiV1DomainsDnszonesCreateOrganizationIdErrorComponent
                | ApiV1DomainsDnszonesCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDnszonesCreatePlatformServiceErrorComponent
                | ApiV1DomainsDnszonesCreatePowerdnsMetadataErrorComponent
                | ApiV1DomainsDnszonesCreatePrimaryZoneErrorComponent
                | ApiV1DomainsDnszonesCreateProviderErrorComponent
                | ApiV1DomainsDnszonesCreateProviderIdErrorComponent
                | ApiV1DomainsDnszonesCreateProviderReferenceErrorComponent
                | ApiV1DomainsDnszonesCreateReconciliationEnabledErrorComponent
                | ApiV1DomainsDnszonesCreateSlaAvailabilityErrorComponent
                | ApiV1DomainsDnszonesCreateSlaTargetErrorComponent
                | ApiV1DomainsDnszonesCreateSlaWindowDaysErrorComponent
                | ApiV1DomainsDnszonesCreateSloAvailabilityErrorComponent
                | ApiV1DomainsDnszonesCreateSloTargetErrorComponent
                | ApiV1DomainsDnszonesCreateSloWindowDaysErrorComponent
                | ApiV1DomainsDnszonesCreateSyncFromErrorComponent
                | ApiV1DomainsDnszonesCreateTargetAvailabilityErrorComponent
                | ApiV1DomainsDnszonesCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_0 = (
                        ApiV1DomainsDnszonesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_1 = (
                        ApiV1DomainsDnszonesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_2 = (
                        ApiV1DomainsDnszonesCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_3 = (
                        ApiV1DomainsDnszonesCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_4 = (
                        ApiV1DomainsDnszonesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_5 = (
                        ApiV1DomainsDnszonesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_6 = (
                        ApiV1DomainsDnszonesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_7 = (
                        ApiV1DomainsDnszonesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_8 = (
                        ApiV1DomainsDnszonesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_9 = (
                        ApiV1DomainsDnszonesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_10 = (
                        ApiV1DomainsDnszonesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_11 = (
                        ApiV1DomainsDnszonesCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_12 = (
                        ApiV1DomainsDnszonesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_13 = (
                        ApiV1DomainsDnszonesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_14 = (
                        ApiV1DomainsDnszonesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_15 = (
                        ApiV1DomainsDnszonesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_16 = (
                        ApiV1DomainsDnszonesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_17 = (
                        ApiV1DomainsDnszonesCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_18 = (
                        ApiV1DomainsDnszonesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_19 = (
                        ApiV1DomainsDnszonesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_20 = (
                        ApiV1DomainsDnszonesCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_21 = (
                        ApiV1DomainsDnszonesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_22 = (
                        ApiV1DomainsDnszonesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_23 = (
                        ApiV1DomainsDnszonesCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_24 = (
                        ApiV1DomainsDnszonesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_25 = (
                        ApiV1DomainsDnszonesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_26 = (
                        ApiV1DomainsDnszonesCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_27 = (
                        ApiV1DomainsDnszonesCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_28 = (
                        ApiV1DomainsDnszonesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_29 = (
                        ApiV1DomainsDnszonesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_30 = (
                        ApiV1DomainsDnszonesCreatePrimaryZoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_31 = (
                        ApiV1DomainsDnszonesCreatePowerdnsMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_32 = (
                        ApiV1DomainsDnszonesCreateDefaultTtlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_33 = (
                        ApiV1DomainsDnszonesCreateDnssecEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_34 = (
                        ApiV1DomainsDnszonesCreateDnssecAlgorithmErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_35 = (
                        ApiV1DomainsDnszonesCreateDnssecNsec3ErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_36 = (
                        ApiV1DomainsDnszonesCreateDnssecDsRecordsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_37 = (
                        ApiV1DomainsDnszonesCreateDnssecCryptokeysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_38 = (
                        ApiV1DomainsDnszonesCreateNsDelegationSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_39 = (
                        ApiV1DomainsDnszonesCreateDsDelegationSyncedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_40 = (
                        ApiV1DomainsDnszonesCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_41 = (
                        ApiV1DomainsDnszonesCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_42 = (
                        ApiV1DomainsDnszonesCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_dnszones_create_error_type_43 = (
                        ApiV1DomainsDnszonesCreateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_dnszones_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_dnszones_create_error_type_44 = (
                    ApiV1DomainsDnszonesCreateSyncFromErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_dnszones_create_error_type_44

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_dnszones_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_dnszones_create_validation_error.additional_properties = d
        return api_v1_domains_dnszones_create_validation_error

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
