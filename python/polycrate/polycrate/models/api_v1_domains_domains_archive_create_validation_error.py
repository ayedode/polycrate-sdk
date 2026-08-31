from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_domains_archive_create_admin_contact_id_error_component import (
        ApiV1DomainsDomainsArchiveCreateAdminContactIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_annotations_error_component import (
        ApiV1DomainsDomainsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_archived_at_error_component import (
        ApiV1DomainsDomainsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_archived_by_error_component import (
        ApiV1DomainsDomainsArchiveCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_archived_error_component import (
        ApiV1DomainsDomainsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_archived_reason_error_component import (
        ApiV1DomainsDomainsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_auth_code_credential_id_error_component import (
        ApiV1DomainsDomainsArchiveCreateAuthCodeCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_created_by_component_error_component import (
        ApiV1DomainsDomainsArchiveCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_created_by_user_error_component import (
        ApiV1DomainsDomainsArchiveCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_criticality_error_component import (
        ApiV1DomainsDomainsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_debug_mode_error_component import (
        ApiV1DomainsDomainsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_display_name_error_component import (
        ApiV1DomainsDomainsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_dns_zone_id_error_component import (
        ApiV1DomainsDomainsArchiveCreateDnsZoneIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_expiry_date_error_component import (
        ApiV1DomainsDomainsArchiveCreateExpiryDateErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_kind_error_component import (
        ApiV1DomainsDomainsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_labels_error_component import (
        ApiV1DomainsDomainsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDomainsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_managed_by_content_type_error_component import (
        ApiV1DomainsDomainsArchiveCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_managed_by_object_id_error_component import (
        ApiV1DomainsDomainsArchiveCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_modified_by_user_error_component import (
        ApiV1DomainsDomainsArchiveCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_name_error_component import (
        ApiV1DomainsDomainsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_nameservers_error_component import (
        ApiV1DomainsDomainsArchiveCreateNameserversErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_non_field_errors_error_component import (
        ApiV1DomainsDomainsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_owner_contact_id_error_component import (
        ApiV1DomainsDomainsArchiveCreateOwnerContactIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_platform_dns_record_created_error_component import (
        ApiV1DomainsDomainsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_platform_service_error_component import (
        ApiV1DomainsDomainsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_provider_error_component import (
        ApiV1DomainsDomainsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_provider_id_error_component import (
        ApiV1DomainsDomainsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_provider_reference_error_component import (
        ApiV1DomainsDomainsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_provider_status_error_component import (
        ApiV1DomainsDomainsArchiveCreateProviderStatusErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_reconciliation_enabled_error_component import (
        ApiV1DomainsDomainsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_registrar_domain_id_error_component import (
        ApiV1DomainsDomainsArchiveCreateRegistrarDomainIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_registrar_id_error_component import (
        ApiV1DomainsDomainsArchiveCreateRegistrarIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_registrar_metadata_error_component import (
        ApiV1DomainsDomainsArchiveCreateRegistrarMetadataErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_renewal_mode_error_component import (
        ApiV1DomainsDomainsArchiveCreateRenewalModeErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_sla_availability_error_component import (
        ApiV1DomainsDomainsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_sla_target_error_component import (
        ApiV1DomainsDomainsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_sla_window_days_error_component import (
        ApiV1DomainsDomainsArchiveCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_slo_availability_error_component import (
        ApiV1DomainsDomainsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_slo_target_error_component import (
        ApiV1DomainsDomainsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_slo_window_days_error_component import (
        ApiV1DomainsDomainsArchiveCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_target_availability_error_component import (
        ApiV1DomainsDomainsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_tech_contact_id_error_component import (
        ApiV1DomainsDomainsArchiveCreateTechContactIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_tolerations_error_component import (
        ApiV1DomainsDomainsArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_transfer_lock_error_component import (
        ApiV1DomainsDomainsArchiveCreateTransferLockErrorComponent,
    )
    from ..models.api_v1_domains_domains_archive_create_use_platform_dns_error_component import (
        ApiV1DomainsDomainsArchiveCreateUsePlatformDnsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDomainsArchiveCreateValidationError")


@_attrs_define
class ApiV1DomainsDomainsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDomainsArchiveCreateAdminContactIdErrorComponent |
            ApiV1DomainsDomainsArchiveCreateAnnotationsErrorComponent |
            ApiV1DomainsDomainsArchiveCreateArchivedAtErrorComponent |
            ApiV1DomainsDomainsArchiveCreateArchivedByErrorComponent |
            ApiV1DomainsDomainsArchiveCreateArchivedErrorComponent |
            ApiV1DomainsDomainsArchiveCreateArchivedReasonErrorComponent |
            ApiV1DomainsDomainsArchiveCreateAuthCodeCredentialIdErrorComponent |
            ApiV1DomainsDomainsArchiveCreateCreatedByComponentErrorComponent |
            ApiV1DomainsDomainsArchiveCreateCreatedByUserErrorComponent |
            ApiV1DomainsDomainsArchiveCreateCriticalityErrorComponent |
            ApiV1DomainsDomainsArchiveCreateDebugModeErrorComponent |
            ApiV1DomainsDomainsArchiveCreateDisplayNameErrorComponent |
            ApiV1DomainsDomainsArchiveCreateDnsZoneIdErrorComponent |
            ApiV1DomainsDomainsArchiveCreateExpiryDateErrorComponent | ApiV1DomainsDomainsArchiveCreateKindErrorComponent |
            ApiV1DomainsDomainsArchiveCreateLabelsErrorComponent |
            ApiV1DomainsDomainsArchiveCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDomainsArchiveCreateManagedByContentTypeErrorComponent |
            ApiV1DomainsDomainsArchiveCreateManagedByObjectIdErrorComponent |
            ApiV1DomainsDomainsArchiveCreateModifiedByUserErrorComponent |
            ApiV1DomainsDomainsArchiveCreateNameErrorComponent | ApiV1DomainsDomainsArchiveCreateNameserversErrorComponent |
            ApiV1DomainsDomainsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1DomainsDomainsArchiveCreateOwnerContactIdErrorComponent |
            ApiV1DomainsDomainsArchiveCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDomainsArchiveCreatePlatformServiceErrorComponent |
            ApiV1DomainsDomainsArchiveCreateProviderErrorComponent |
            ApiV1DomainsDomainsArchiveCreateProviderIdErrorComponent |
            ApiV1DomainsDomainsArchiveCreateProviderReferenceErrorComponent |
            ApiV1DomainsDomainsArchiveCreateProviderStatusErrorComponent |
            ApiV1DomainsDomainsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1DomainsDomainsArchiveCreateRegistrarDomainIdErrorComponent |
            ApiV1DomainsDomainsArchiveCreateRegistrarIdErrorComponent |
            ApiV1DomainsDomainsArchiveCreateRegistrarMetadataErrorComponent |
            ApiV1DomainsDomainsArchiveCreateRenewalModeErrorComponent |
            ApiV1DomainsDomainsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1DomainsDomainsArchiveCreateSlaTargetErrorComponent |
            ApiV1DomainsDomainsArchiveCreateSlaWindowDaysErrorComponent |
            ApiV1DomainsDomainsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1DomainsDomainsArchiveCreateSloTargetErrorComponent |
            ApiV1DomainsDomainsArchiveCreateSloWindowDaysErrorComponent |
            ApiV1DomainsDomainsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1DomainsDomainsArchiveCreateTechContactIdErrorComponent |
            ApiV1DomainsDomainsArchiveCreateTolerationsErrorComponent |
            ApiV1DomainsDomainsArchiveCreateTransferLockErrorComponent |
            ApiV1DomainsDomainsArchiveCreateUsePlatformDnsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDomainsArchiveCreateAdminContactIdErrorComponent
        | ApiV1DomainsDomainsArchiveCreateAnnotationsErrorComponent
        | ApiV1DomainsDomainsArchiveCreateArchivedAtErrorComponent
        | ApiV1DomainsDomainsArchiveCreateArchivedByErrorComponent
        | ApiV1DomainsDomainsArchiveCreateArchivedErrorComponent
        | ApiV1DomainsDomainsArchiveCreateArchivedReasonErrorComponent
        | ApiV1DomainsDomainsArchiveCreateAuthCodeCredentialIdErrorComponent
        | ApiV1DomainsDomainsArchiveCreateCreatedByComponentErrorComponent
        | ApiV1DomainsDomainsArchiveCreateCreatedByUserErrorComponent
        | ApiV1DomainsDomainsArchiveCreateCriticalityErrorComponent
        | ApiV1DomainsDomainsArchiveCreateDebugModeErrorComponent
        | ApiV1DomainsDomainsArchiveCreateDisplayNameErrorComponent
        | ApiV1DomainsDomainsArchiveCreateDnsZoneIdErrorComponent
        | ApiV1DomainsDomainsArchiveCreateExpiryDateErrorComponent
        | ApiV1DomainsDomainsArchiveCreateKindErrorComponent
        | ApiV1DomainsDomainsArchiveCreateLabelsErrorComponent
        | ApiV1DomainsDomainsArchiveCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDomainsArchiveCreateManagedByContentTypeErrorComponent
        | ApiV1DomainsDomainsArchiveCreateManagedByObjectIdErrorComponent
        | ApiV1DomainsDomainsArchiveCreateModifiedByUserErrorComponent
        | ApiV1DomainsDomainsArchiveCreateNameErrorComponent
        | ApiV1DomainsDomainsArchiveCreateNameserversErrorComponent
        | ApiV1DomainsDomainsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1DomainsDomainsArchiveCreateOwnerContactIdErrorComponent
        | ApiV1DomainsDomainsArchiveCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDomainsArchiveCreatePlatformServiceErrorComponent
        | ApiV1DomainsDomainsArchiveCreateProviderErrorComponent
        | ApiV1DomainsDomainsArchiveCreateProviderIdErrorComponent
        | ApiV1DomainsDomainsArchiveCreateProviderReferenceErrorComponent
        | ApiV1DomainsDomainsArchiveCreateProviderStatusErrorComponent
        | ApiV1DomainsDomainsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1DomainsDomainsArchiveCreateRegistrarDomainIdErrorComponent
        | ApiV1DomainsDomainsArchiveCreateRegistrarIdErrorComponent
        | ApiV1DomainsDomainsArchiveCreateRegistrarMetadataErrorComponent
        | ApiV1DomainsDomainsArchiveCreateRenewalModeErrorComponent
        | ApiV1DomainsDomainsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1DomainsDomainsArchiveCreateSlaTargetErrorComponent
        | ApiV1DomainsDomainsArchiveCreateSlaWindowDaysErrorComponent
        | ApiV1DomainsDomainsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1DomainsDomainsArchiveCreateSloTargetErrorComponent
        | ApiV1DomainsDomainsArchiveCreateSloWindowDaysErrorComponent
        | ApiV1DomainsDomainsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1DomainsDomainsArchiveCreateTechContactIdErrorComponent
        | ApiV1DomainsDomainsArchiveCreateTolerationsErrorComponent
        | ApiV1DomainsDomainsArchiveCreateTransferLockErrorComponent
        | ApiV1DomainsDomainsArchiveCreateUsePlatformDnsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_domains_archive_create_admin_contact_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateAdminContactIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_annotations_error_component import (
            ApiV1DomainsDomainsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_archived_at_error_component import (
            ApiV1DomainsDomainsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_archived_by_error_component import (
            ApiV1DomainsDomainsArchiveCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_archived_error_component import (
            ApiV1DomainsDomainsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_archived_reason_error_component import (
            ApiV1DomainsDomainsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_auth_code_credential_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateAuthCodeCredentialIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_created_by_component_error_component import (
            ApiV1DomainsDomainsArchiveCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_criticality_error_component import (
            ApiV1DomainsDomainsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_debug_mode_error_component import (
            ApiV1DomainsDomainsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_display_name_error_component import (
            ApiV1DomainsDomainsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_dns_zone_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateDnsZoneIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_expiry_date_error_component import (
            ApiV1DomainsDomainsArchiveCreateExpiryDateErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_kind_error_component import (
            ApiV1DomainsDomainsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_labels_error_component import (
            ApiV1DomainsDomainsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_managed_by_content_type_error_component import (
            ApiV1DomainsDomainsArchiveCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_managed_by_object_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_modified_by_user_error_component import (
            ApiV1DomainsDomainsArchiveCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_name_error_component import (
            ApiV1DomainsDomainsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_nameservers_error_component import (
            ApiV1DomainsDomainsArchiveCreateNameserversErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_non_field_errors_error_component import (
            ApiV1DomainsDomainsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_owner_contact_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateOwnerContactIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_platform_service_error_component import (
            ApiV1DomainsDomainsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_provider_error_component import (
            ApiV1DomainsDomainsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_provider_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_provider_reference_error_component import (
            ApiV1DomainsDomainsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_provider_status_error_component import (
            ApiV1DomainsDomainsArchiveCreateProviderStatusErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_registrar_domain_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateRegistrarDomainIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_registrar_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateRegistrarIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_registrar_metadata_error_component import (
            ApiV1DomainsDomainsArchiveCreateRegistrarMetadataErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_renewal_mode_error_component import (
            ApiV1DomainsDomainsArchiveCreateRenewalModeErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_sla_availability_error_component import (
            ApiV1DomainsDomainsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_sla_target_error_component import (
            ApiV1DomainsDomainsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_sla_window_days_error_component import (
            ApiV1DomainsDomainsArchiveCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_slo_availability_error_component import (
            ApiV1DomainsDomainsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_slo_target_error_component import (
            ApiV1DomainsDomainsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_slo_window_days_error_component import (
            ApiV1DomainsDomainsArchiveCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_target_availability_error_component import (
            ApiV1DomainsDomainsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_tech_contact_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateTechContactIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_tolerations_error_component import (
            ApiV1DomainsDomainsArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_transfer_lock_error_component import (
            ApiV1DomainsDomainsArchiveCreateTransferLockErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_use_platform_dns_error_component import (
            ApiV1DomainsDomainsArchiveCreateUsePlatformDnsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateRegistrarIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateDnsZoneIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateUsePlatformDnsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateOwnerContactIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateAdminContactIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateTechContactIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateAuthCodeCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DomainsDomainsArchiveCreateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateNameserversErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateRenewalModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateTransferLockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateRegistrarDomainIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateProviderStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateExpiryDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateRegistrarMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsArchiveCreateModifiedByUserErrorComponent):
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
        from ..models.api_v1_domains_domains_archive_create_admin_contact_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateAdminContactIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_annotations_error_component import (
            ApiV1DomainsDomainsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_archived_at_error_component import (
            ApiV1DomainsDomainsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_archived_by_error_component import (
            ApiV1DomainsDomainsArchiveCreateArchivedByErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_archived_error_component import (
            ApiV1DomainsDomainsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_archived_reason_error_component import (
            ApiV1DomainsDomainsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_auth_code_credential_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateAuthCodeCredentialIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_created_by_component_error_component import (
            ApiV1DomainsDomainsArchiveCreateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_created_by_user_error_component import (
            ApiV1DomainsDomainsArchiveCreateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_criticality_error_component import (
            ApiV1DomainsDomainsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_debug_mode_error_component import (
            ApiV1DomainsDomainsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_display_name_error_component import (
            ApiV1DomainsDomainsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_dns_zone_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateDnsZoneIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_expiry_date_error_component import (
            ApiV1DomainsDomainsArchiveCreateExpiryDateErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_kind_error_component import (
            ApiV1DomainsDomainsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_labels_error_component import (
            ApiV1DomainsDomainsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainsArchiveCreateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_managed_by_content_type_error_component import (
            ApiV1DomainsDomainsArchiveCreateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_managed_by_object_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_modified_by_user_error_component import (
            ApiV1DomainsDomainsArchiveCreateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_name_error_component import (
            ApiV1DomainsDomainsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_nameservers_error_component import (
            ApiV1DomainsDomainsArchiveCreateNameserversErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_non_field_errors_error_component import (
            ApiV1DomainsDomainsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_owner_contact_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateOwnerContactIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainsArchiveCreatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_platform_service_error_component import (
            ApiV1DomainsDomainsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_provider_error_component import (
            ApiV1DomainsDomainsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_provider_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_provider_reference_error_component import (
            ApiV1DomainsDomainsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_provider_status_error_component import (
            ApiV1DomainsDomainsArchiveCreateProviderStatusErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_registrar_domain_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateRegistrarDomainIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_registrar_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateRegistrarIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_registrar_metadata_error_component import (
            ApiV1DomainsDomainsArchiveCreateRegistrarMetadataErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_renewal_mode_error_component import (
            ApiV1DomainsDomainsArchiveCreateRenewalModeErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_sla_availability_error_component import (
            ApiV1DomainsDomainsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_sla_target_error_component import (
            ApiV1DomainsDomainsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_sla_window_days_error_component import (
            ApiV1DomainsDomainsArchiveCreateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_slo_availability_error_component import (
            ApiV1DomainsDomainsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_slo_target_error_component import (
            ApiV1DomainsDomainsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_slo_window_days_error_component import (
            ApiV1DomainsDomainsArchiveCreateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_target_availability_error_component import (
            ApiV1DomainsDomainsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_tech_contact_id_error_component import (
            ApiV1DomainsDomainsArchiveCreateTechContactIdErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_tolerations_error_component import (
            ApiV1DomainsDomainsArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_transfer_lock_error_component import (
            ApiV1DomainsDomainsArchiveCreateTransferLockErrorComponent,
        )
        from ..models.api_v1_domains_domains_archive_create_use_platform_dns_error_component import (
            ApiV1DomainsDomainsArchiveCreateUsePlatformDnsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDomainsArchiveCreateAdminContactIdErrorComponent
                | ApiV1DomainsDomainsArchiveCreateAnnotationsErrorComponent
                | ApiV1DomainsDomainsArchiveCreateArchivedAtErrorComponent
                | ApiV1DomainsDomainsArchiveCreateArchivedByErrorComponent
                | ApiV1DomainsDomainsArchiveCreateArchivedErrorComponent
                | ApiV1DomainsDomainsArchiveCreateArchivedReasonErrorComponent
                | ApiV1DomainsDomainsArchiveCreateAuthCodeCredentialIdErrorComponent
                | ApiV1DomainsDomainsArchiveCreateCreatedByComponentErrorComponent
                | ApiV1DomainsDomainsArchiveCreateCreatedByUserErrorComponent
                | ApiV1DomainsDomainsArchiveCreateCriticalityErrorComponent
                | ApiV1DomainsDomainsArchiveCreateDebugModeErrorComponent
                | ApiV1DomainsDomainsArchiveCreateDisplayNameErrorComponent
                | ApiV1DomainsDomainsArchiveCreateDnsZoneIdErrorComponent
                | ApiV1DomainsDomainsArchiveCreateExpiryDateErrorComponent
                | ApiV1DomainsDomainsArchiveCreateKindErrorComponent
                | ApiV1DomainsDomainsArchiveCreateLabelsErrorComponent
                | ApiV1DomainsDomainsArchiveCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDomainsArchiveCreateManagedByContentTypeErrorComponent
                | ApiV1DomainsDomainsArchiveCreateManagedByObjectIdErrorComponent
                | ApiV1DomainsDomainsArchiveCreateModifiedByUserErrorComponent
                | ApiV1DomainsDomainsArchiveCreateNameErrorComponent
                | ApiV1DomainsDomainsArchiveCreateNameserversErrorComponent
                | ApiV1DomainsDomainsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1DomainsDomainsArchiveCreateOwnerContactIdErrorComponent
                | ApiV1DomainsDomainsArchiveCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDomainsArchiveCreatePlatformServiceErrorComponent
                | ApiV1DomainsDomainsArchiveCreateProviderErrorComponent
                | ApiV1DomainsDomainsArchiveCreateProviderIdErrorComponent
                | ApiV1DomainsDomainsArchiveCreateProviderReferenceErrorComponent
                | ApiV1DomainsDomainsArchiveCreateProviderStatusErrorComponent
                | ApiV1DomainsDomainsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1DomainsDomainsArchiveCreateRegistrarDomainIdErrorComponent
                | ApiV1DomainsDomainsArchiveCreateRegistrarIdErrorComponent
                | ApiV1DomainsDomainsArchiveCreateRegistrarMetadataErrorComponent
                | ApiV1DomainsDomainsArchiveCreateRenewalModeErrorComponent
                | ApiV1DomainsDomainsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1DomainsDomainsArchiveCreateSlaTargetErrorComponent
                | ApiV1DomainsDomainsArchiveCreateSlaWindowDaysErrorComponent
                | ApiV1DomainsDomainsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1DomainsDomainsArchiveCreateSloTargetErrorComponent
                | ApiV1DomainsDomainsArchiveCreateSloWindowDaysErrorComponent
                | ApiV1DomainsDomainsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1DomainsDomainsArchiveCreateTechContactIdErrorComponent
                | ApiV1DomainsDomainsArchiveCreateTolerationsErrorComponent
                | ApiV1DomainsDomainsArchiveCreateTransferLockErrorComponent
                | ApiV1DomainsDomainsArchiveCreateUsePlatformDnsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_0 = (
                        ApiV1DomainsDomainsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_1 = (
                        ApiV1DomainsDomainsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_2 = (
                        ApiV1DomainsDomainsArchiveCreateRegistrarIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_3 = (
                        ApiV1DomainsDomainsArchiveCreateDnsZoneIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_4 = (
                        ApiV1DomainsDomainsArchiveCreateUsePlatformDnsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_5 = (
                        ApiV1DomainsDomainsArchiveCreateOwnerContactIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_6 = (
                        ApiV1DomainsDomainsArchiveCreateAdminContactIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_7 = (
                        ApiV1DomainsDomainsArchiveCreateTechContactIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_8 = (
                        ApiV1DomainsDomainsArchiveCreateAuthCodeCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_9 = (
                        ApiV1DomainsDomainsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_10 = (
                        ApiV1DomainsDomainsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_11 = (
                        ApiV1DomainsDomainsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_12 = (
                        ApiV1DomainsDomainsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_13 = (
                        ApiV1DomainsDomainsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_14 = (
                        ApiV1DomainsDomainsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_15 = (
                        ApiV1DomainsDomainsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_16 = (
                        ApiV1DomainsDomainsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_17 = (
                        ApiV1DomainsDomainsArchiveCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_18 = (
                        ApiV1DomainsDomainsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_19 = (
                        ApiV1DomainsDomainsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_20 = (
                        ApiV1DomainsDomainsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_21 = (
                        ApiV1DomainsDomainsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_22 = (
                        ApiV1DomainsDomainsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_23 = (
                        ApiV1DomainsDomainsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_24 = (
                        ApiV1DomainsDomainsArchiveCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_25 = (
                        ApiV1DomainsDomainsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_26 = (
                        ApiV1DomainsDomainsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_27 = (
                        ApiV1DomainsDomainsArchiveCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_28 = (
                        ApiV1DomainsDomainsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_29 = (
                        ApiV1DomainsDomainsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_30 = (
                        ApiV1DomainsDomainsArchiveCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_31 = (
                        ApiV1DomainsDomainsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_32 = (
                        ApiV1DomainsDomainsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_33 = (
                        ApiV1DomainsDomainsArchiveCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_34 = (
                        ApiV1DomainsDomainsArchiveCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_35 = (
                        ApiV1DomainsDomainsArchiveCreateNameserversErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_36 = (
                        ApiV1DomainsDomainsArchiveCreateRenewalModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_37 = (
                        ApiV1DomainsDomainsArchiveCreateTransferLockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_38 = (
                        ApiV1DomainsDomainsArchiveCreateRegistrarDomainIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_39 = (
                        ApiV1DomainsDomainsArchiveCreateProviderStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_40 = (
                        ApiV1DomainsDomainsArchiveCreateExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_41 = (
                        ApiV1DomainsDomainsArchiveCreateRegistrarMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_42 = (
                        ApiV1DomainsDomainsArchiveCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_43 = (
                        ApiV1DomainsDomainsArchiveCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_archive_create_error_type_44 = (
                        ApiV1DomainsDomainsArchiveCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_domains_archive_create_error_type_45 = (
                    ApiV1DomainsDomainsArchiveCreateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_domains_archive_create_error_type_45

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_domains_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_domains_archive_create_validation_error.additional_properties = d
        return api_v1_domains_domains_archive_create_validation_error

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
