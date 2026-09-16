from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_domains_domains_create_admin_contact_id_error_component import (
        ApiV1DomainsDomainsCreateAdminContactIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_annotations_error_component import (
        ApiV1DomainsDomainsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_archived_at_error_component import (
        ApiV1DomainsDomainsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_archived_by_error_component import (
        ApiV1DomainsDomainsCreateArchivedByErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_archived_error_component import (
        ApiV1DomainsDomainsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_archived_reason_error_component import (
        ApiV1DomainsDomainsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_auth_code_credential_id_error_component import (
        ApiV1DomainsDomainsCreateAuthCodeCredentialIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_created_by_component_error_component import (
        ApiV1DomainsDomainsCreateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_created_by_user_error_component import (
        ApiV1DomainsDomainsCreateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_criticality_error_component import (
        ApiV1DomainsDomainsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_debug_mode_error_component import (
        ApiV1DomainsDomainsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_display_name_error_component import (
        ApiV1DomainsDomainsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_dns_zone_id_error_component import (
        ApiV1DomainsDomainsCreateDnsZoneIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_expiry_date_error_component import (
        ApiV1DomainsDomainsCreateExpiryDateErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_kind_error_component import ApiV1DomainsDomainsCreateKindErrorComponent
    from ..models.api_v1_domains_domains_create_labels_error_component import (
        ApiV1DomainsDomainsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_last_reconciliation_duration_seconds_error_component import (
        ApiV1DomainsDomainsCreateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_managed_by_content_type_error_component import (
        ApiV1DomainsDomainsCreateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_managed_by_object_id_error_component import (
        ApiV1DomainsDomainsCreateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_modified_by_user_error_component import (
        ApiV1DomainsDomainsCreateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_name_error_component import ApiV1DomainsDomainsCreateNameErrorComponent
    from ..models.api_v1_domains_domains_create_nameservers_error_component import (
        ApiV1DomainsDomainsCreateNameserversErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_non_field_errors_error_component import (
        ApiV1DomainsDomainsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_owner_contact_id_error_component import (
        ApiV1DomainsDomainsCreateOwnerContactIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_platform_dns_record_created_error_component import (
        ApiV1DomainsDomainsCreatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_platform_service_error_component import (
        ApiV1DomainsDomainsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_provider_error_component import (
        ApiV1DomainsDomainsCreateProviderErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_provider_id_error_component import (
        ApiV1DomainsDomainsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_provider_reference_error_component import (
        ApiV1DomainsDomainsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_provider_status_error_component import (
        ApiV1DomainsDomainsCreateProviderStatusErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_reconciliation_enabled_error_component import (
        ApiV1DomainsDomainsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_registrar_domain_id_error_component import (
        ApiV1DomainsDomainsCreateRegistrarDomainIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_registrar_id_error_component import (
        ApiV1DomainsDomainsCreateRegistrarIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_registrar_metadata_error_component import (
        ApiV1DomainsDomainsCreateRegistrarMetadataErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_renewal_mode_error_component import (
        ApiV1DomainsDomainsCreateRenewalModeErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_sla_availability_error_component import (
        ApiV1DomainsDomainsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_sla_target_error_component import (
        ApiV1DomainsDomainsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_sla_window_days_error_component import (
        ApiV1DomainsDomainsCreateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_slo_availability_error_component import (
        ApiV1DomainsDomainsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_slo_target_error_component import (
        ApiV1DomainsDomainsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_slo_window_days_error_component import (
        ApiV1DomainsDomainsCreateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_target_availability_error_component import (
        ApiV1DomainsDomainsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_tech_contact_id_error_component import (
        ApiV1DomainsDomainsCreateTechContactIdErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_tolerations_error_component import (
        ApiV1DomainsDomainsCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_transfer_lock_error_component import (
        ApiV1DomainsDomainsCreateTransferLockErrorComponent,
    )
    from ..models.api_v1_domains_domains_create_use_platform_dns_error_component import (
        ApiV1DomainsDomainsCreateUsePlatformDnsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DomainsDomainsCreateValidationError")


@_attrs_define
class ApiV1DomainsDomainsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DomainsDomainsCreateAdminContactIdErrorComponent |
            ApiV1DomainsDomainsCreateAnnotationsErrorComponent | ApiV1DomainsDomainsCreateArchivedAtErrorComponent |
            ApiV1DomainsDomainsCreateArchivedByErrorComponent | ApiV1DomainsDomainsCreateArchivedErrorComponent |
            ApiV1DomainsDomainsCreateArchivedReasonErrorComponent |
            ApiV1DomainsDomainsCreateAuthCodeCredentialIdErrorComponent |
            ApiV1DomainsDomainsCreateCreatedByComponentErrorComponent | ApiV1DomainsDomainsCreateCreatedByUserErrorComponent
            | ApiV1DomainsDomainsCreateCriticalityErrorComponent | ApiV1DomainsDomainsCreateDebugModeErrorComponent |
            ApiV1DomainsDomainsCreateDisplayNameErrorComponent | ApiV1DomainsDomainsCreateDnsZoneIdErrorComponent |
            ApiV1DomainsDomainsCreateExpiryDateErrorComponent | ApiV1DomainsDomainsCreateKindErrorComponent |
            ApiV1DomainsDomainsCreateLabelsErrorComponent |
            ApiV1DomainsDomainsCreateLastReconciliationDurationSecondsErrorComponent |
            ApiV1DomainsDomainsCreateManagedByContentTypeErrorComponent |
            ApiV1DomainsDomainsCreateManagedByObjectIdErrorComponent | ApiV1DomainsDomainsCreateModifiedByUserErrorComponent
            | ApiV1DomainsDomainsCreateNameErrorComponent | ApiV1DomainsDomainsCreateNameserversErrorComponent |
            ApiV1DomainsDomainsCreateNonFieldErrorsErrorComponent | ApiV1DomainsDomainsCreateOwnerContactIdErrorComponent |
            ApiV1DomainsDomainsCreatePlatformDnsRecordCreatedErrorComponent |
            ApiV1DomainsDomainsCreatePlatformServiceErrorComponent | ApiV1DomainsDomainsCreateProviderErrorComponent |
            ApiV1DomainsDomainsCreateProviderIdErrorComponent | ApiV1DomainsDomainsCreateProviderReferenceErrorComponent |
            ApiV1DomainsDomainsCreateProviderStatusErrorComponent |
            ApiV1DomainsDomainsCreateReconciliationEnabledErrorComponent |
            ApiV1DomainsDomainsCreateRegistrarDomainIdErrorComponent | ApiV1DomainsDomainsCreateRegistrarIdErrorComponent |
            ApiV1DomainsDomainsCreateRegistrarMetadataErrorComponent | ApiV1DomainsDomainsCreateRenewalModeErrorComponent |
            ApiV1DomainsDomainsCreateSlaAvailabilityErrorComponent | ApiV1DomainsDomainsCreateSlaTargetErrorComponent |
            ApiV1DomainsDomainsCreateSlaWindowDaysErrorComponent | ApiV1DomainsDomainsCreateSloAvailabilityErrorComponent |
            ApiV1DomainsDomainsCreateSloTargetErrorComponent | ApiV1DomainsDomainsCreateSloWindowDaysErrorComponent |
            ApiV1DomainsDomainsCreateTargetAvailabilityErrorComponent | ApiV1DomainsDomainsCreateTechContactIdErrorComponent
            | ApiV1DomainsDomainsCreateTolerationsErrorComponent | ApiV1DomainsDomainsCreateTransferLockErrorComponent |
            ApiV1DomainsDomainsCreateUsePlatformDnsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DomainsDomainsCreateAdminContactIdErrorComponent
        | ApiV1DomainsDomainsCreateAnnotationsErrorComponent
        | ApiV1DomainsDomainsCreateArchivedAtErrorComponent
        | ApiV1DomainsDomainsCreateArchivedByErrorComponent
        | ApiV1DomainsDomainsCreateArchivedErrorComponent
        | ApiV1DomainsDomainsCreateArchivedReasonErrorComponent
        | ApiV1DomainsDomainsCreateAuthCodeCredentialIdErrorComponent
        | ApiV1DomainsDomainsCreateCreatedByComponentErrorComponent
        | ApiV1DomainsDomainsCreateCreatedByUserErrorComponent
        | ApiV1DomainsDomainsCreateCriticalityErrorComponent
        | ApiV1DomainsDomainsCreateDebugModeErrorComponent
        | ApiV1DomainsDomainsCreateDisplayNameErrorComponent
        | ApiV1DomainsDomainsCreateDnsZoneIdErrorComponent
        | ApiV1DomainsDomainsCreateExpiryDateErrorComponent
        | ApiV1DomainsDomainsCreateKindErrorComponent
        | ApiV1DomainsDomainsCreateLabelsErrorComponent
        | ApiV1DomainsDomainsCreateLastReconciliationDurationSecondsErrorComponent
        | ApiV1DomainsDomainsCreateManagedByContentTypeErrorComponent
        | ApiV1DomainsDomainsCreateManagedByObjectIdErrorComponent
        | ApiV1DomainsDomainsCreateModifiedByUserErrorComponent
        | ApiV1DomainsDomainsCreateNameErrorComponent
        | ApiV1DomainsDomainsCreateNameserversErrorComponent
        | ApiV1DomainsDomainsCreateNonFieldErrorsErrorComponent
        | ApiV1DomainsDomainsCreateOwnerContactIdErrorComponent
        | ApiV1DomainsDomainsCreatePlatformDnsRecordCreatedErrorComponent
        | ApiV1DomainsDomainsCreatePlatformServiceErrorComponent
        | ApiV1DomainsDomainsCreateProviderErrorComponent
        | ApiV1DomainsDomainsCreateProviderIdErrorComponent
        | ApiV1DomainsDomainsCreateProviderReferenceErrorComponent
        | ApiV1DomainsDomainsCreateProviderStatusErrorComponent
        | ApiV1DomainsDomainsCreateReconciliationEnabledErrorComponent
        | ApiV1DomainsDomainsCreateRegistrarDomainIdErrorComponent
        | ApiV1DomainsDomainsCreateRegistrarIdErrorComponent
        | ApiV1DomainsDomainsCreateRegistrarMetadataErrorComponent
        | ApiV1DomainsDomainsCreateRenewalModeErrorComponent
        | ApiV1DomainsDomainsCreateSlaAvailabilityErrorComponent
        | ApiV1DomainsDomainsCreateSlaTargetErrorComponent
        | ApiV1DomainsDomainsCreateSlaWindowDaysErrorComponent
        | ApiV1DomainsDomainsCreateSloAvailabilityErrorComponent
        | ApiV1DomainsDomainsCreateSloTargetErrorComponent
        | ApiV1DomainsDomainsCreateSloWindowDaysErrorComponent
        | ApiV1DomainsDomainsCreateTargetAvailabilityErrorComponent
        | ApiV1DomainsDomainsCreateTechContactIdErrorComponent
        | ApiV1DomainsDomainsCreateTolerationsErrorComponent
        | ApiV1DomainsDomainsCreateTransferLockErrorComponent
        | ApiV1DomainsDomainsCreateUsePlatformDnsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_domains_domains_create_admin_contact_id_error_component import (
            ApiV1DomainsDomainsCreateAdminContactIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_annotations_error_component import (
            ApiV1DomainsDomainsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_archived_at_error_component import (
            ApiV1DomainsDomainsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_archived_by_error_component import (
            ApiV1DomainsDomainsCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_archived_error_component import (
            ApiV1DomainsDomainsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_archived_reason_error_component import (
            ApiV1DomainsDomainsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_auth_code_credential_id_error_component import (
            ApiV1DomainsDomainsCreateAuthCodeCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_created_by_component_error_component import (
            ApiV1DomainsDomainsCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_criticality_error_component import (
            ApiV1DomainsDomainsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_debug_mode_error_component import (
            ApiV1DomainsDomainsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_display_name_error_component import (
            ApiV1DomainsDomainsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_dns_zone_id_error_component import (
            ApiV1DomainsDomainsCreateDnsZoneIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_expiry_date_error_component import (
            ApiV1DomainsDomainsCreateExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_kind_error_component import (
            ApiV1DomainsDomainsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_labels_error_component import (
            ApiV1DomainsDomainsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainsCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_managed_by_content_type_error_component import (
            ApiV1DomainsDomainsCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_managed_by_object_id_error_component import (
            ApiV1DomainsDomainsCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_modified_by_user_error_component import (
            ApiV1DomainsDomainsCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_name_error_component import (
            ApiV1DomainsDomainsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_nameservers_error_component import (
            ApiV1DomainsDomainsCreateNameserversErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_non_field_errors_error_component import (
            ApiV1DomainsDomainsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_owner_contact_id_error_component import (
            ApiV1DomainsDomainsCreateOwnerContactIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainsCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_platform_service_error_component import (
            ApiV1DomainsDomainsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_provider_error_component import (
            ApiV1DomainsDomainsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_provider_id_error_component import (
            ApiV1DomainsDomainsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_provider_reference_error_component import (
            ApiV1DomainsDomainsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_provider_status_error_component import (
            ApiV1DomainsDomainsCreateProviderStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_registrar_domain_id_error_component import (
            ApiV1DomainsDomainsCreateRegistrarDomainIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_registrar_id_error_component import (
            ApiV1DomainsDomainsCreateRegistrarIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_registrar_metadata_error_component import (
            ApiV1DomainsDomainsCreateRegistrarMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_renewal_mode_error_component import (
            ApiV1DomainsDomainsCreateRenewalModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_sla_availability_error_component import (
            ApiV1DomainsDomainsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_sla_target_error_component import (
            ApiV1DomainsDomainsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_sla_window_days_error_component import (
            ApiV1DomainsDomainsCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_slo_availability_error_component import (
            ApiV1DomainsDomainsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_slo_target_error_component import (
            ApiV1DomainsDomainsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_slo_window_days_error_component import (
            ApiV1DomainsDomainsCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_target_availability_error_component import (
            ApiV1DomainsDomainsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_tech_contact_id_error_component import (
            ApiV1DomainsDomainsCreateTechContactIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_tolerations_error_component import (
            ApiV1DomainsDomainsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_transfer_lock_error_component import (
            ApiV1DomainsDomainsCreateTransferLockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_use_platform_dns_error_component import (
            ApiV1DomainsDomainsCreateUsePlatformDnsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DomainsDomainsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateRegistrarIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateDnsZoneIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateUsePlatformDnsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateOwnerContactIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateAdminContactIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateTechContactIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateAuthCodeCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateLastReconciliationDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateNameserversErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateRenewalModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateTransferLockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateRegistrarDomainIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateProviderStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateExpiryDateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateRegistrarMetadataErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DomainsDomainsCreateModifiedByUserErrorComponent):
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
        from ..models.api_v1_domains_domains_create_admin_contact_id_error_component import (
            ApiV1DomainsDomainsCreateAdminContactIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_annotations_error_component import (
            ApiV1DomainsDomainsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_archived_at_error_component import (
            ApiV1DomainsDomainsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_archived_by_error_component import (
            ApiV1DomainsDomainsCreateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_archived_error_component import (
            ApiV1DomainsDomainsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_archived_reason_error_component import (
            ApiV1DomainsDomainsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_auth_code_credential_id_error_component import (
            ApiV1DomainsDomainsCreateAuthCodeCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_created_by_component_error_component import (
            ApiV1DomainsDomainsCreateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_created_by_user_error_component import (
            ApiV1DomainsDomainsCreateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_criticality_error_component import (
            ApiV1DomainsDomainsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_debug_mode_error_component import (
            ApiV1DomainsDomainsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_display_name_error_component import (
            ApiV1DomainsDomainsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_dns_zone_id_error_component import (
            ApiV1DomainsDomainsCreateDnsZoneIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_expiry_date_error_component import (
            ApiV1DomainsDomainsCreateExpiryDateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_kind_error_component import (
            ApiV1DomainsDomainsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_labels_error_component import (
            ApiV1DomainsDomainsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_last_reconciliation_duration_seconds_error_component import (
            ApiV1DomainsDomainsCreateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_managed_by_content_type_error_component import (
            ApiV1DomainsDomainsCreateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_managed_by_object_id_error_component import (
            ApiV1DomainsDomainsCreateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_modified_by_user_error_component import (
            ApiV1DomainsDomainsCreateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_name_error_component import (
            ApiV1DomainsDomainsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_nameservers_error_component import (
            ApiV1DomainsDomainsCreateNameserversErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_non_field_errors_error_component import (
            ApiV1DomainsDomainsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_owner_contact_id_error_component import (
            ApiV1DomainsDomainsCreateOwnerContactIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_platform_dns_record_created_error_component import (
            ApiV1DomainsDomainsCreatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_platform_service_error_component import (
            ApiV1DomainsDomainsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_provider_error_component import (
            ApiV1DomainsDomainsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_provider_id_error_component import (
            ApiV1DomainsDomainsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_provider_reference_error_component import (
            ApiV1DomainsDomainsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_provider_status_error_component import (
            ApiV1DomainsDomainsCreateProviderStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_reconciliation_enabled_error_component import (
            ApiV1DomainsDomainsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_registrar_domain_id_error_component import (
            ApiV1DomainsDomainsCreateRegistrarDomainIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_registrar_id_error_component import (
            ApiV1DomainsDomainsCreateRegistrarIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_registrar_metadata_error_component import (
            ApiV1DomainsDomainsCreateRegistrarMetadataErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_renewal_mode_error_component import (
            ApiV1DomainsDomainsCreateRenewalModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_sla_availability_error_component import (
            ApiV1DomainsDomainsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_sla_target_error_component import (
            ApiV1DomainsDomainsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_sla_window_days_error_component import (
            ApiV1DomainsDomainsCreateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_slo_availability_error_component import (
            ApiV1DomainsDomainsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_slo_target_error_component import (
            ApiV1DomainsDomainsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_slo_window_days_error_component import (
            ApiV1DomainsDomainsCreateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_target_availability_error_component import (
            ApiV1DomainsDomainsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_tech_contact_id_error_component import (
            ApiV1DomainsDomainsCreateTechContactIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_tolerations_error_component import (
            ApiV1DomainsDomainsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_transfer_lock_error_component import (
            ApiV1DomainsDomainsCreateTransferLockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_domains_domains_create_use_platform_dns_error_component import (
            ApiV1DomainsDomainsCreateUsePlatformDnsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DomainsDomainsCreateAdminContactIdErrorComponent
                | ApiV1DomainsDomainsCreateAnnotationsErrorComponent
                | ApiV1DomainsDomainsCreateArchivedAtErrorComponent
                | ApiV1DomainsDomainsCreateArchivedByErrorComponent
                | ApiV1DomainsDomainsCreateArchivedErrorComponent
                | ApiV1DomainsDomainsCreateArchivedReasonErrorComponent
                | ApiV1DomainsDomainsCreateAuthCodeCredentialIdErrorComponent
                | ApiV1DomainsDomainsCreateCreatedByComponentErrorComponent
                | ApiV1DomainsDomainsCreateCreatedByUserErrorComponent
                | ApiV1DomainsDomainsCreateCriticalityErrorComponent
                | ApiV1DomainsDomainsCreateDebugModeErrorComponent
                | ApiV1DomainsDomainsCreateDisplayNameErrorComponent
                | ApiV1DomainsDomainsCreateDnsZoneIdErrorComponent
                | ApiV1DomainsDomainsCreateExpiryDateErrorComponent
                | ApiV1DomainsDomainsCreateKindErrorComponent
                | ApiV1DomainsDomainsCreateLabelsErrorComponent
                | ApiV1DomainsDomainsCreateLastReconciliationDurationSecondsErrorComponent
                | ApiV1DomainsDomainsCreateManagedByContentTypeErrorComponent
                | ApiV1DomainsDomainsCreateManagedByObjectIdErrorComponent
                | ApiV1DomainsDomainsCreateModifiedByUserErrorComponent
                | ApiV1DomainsDomainsCreateNameErrorComponent
                | ApiV1DomainsDomainsCreateNameserversErrorComponent
                | ApiV1DomainsDomainsCreateNonFieldErrorsErrorComponent
                | ApiV1DomainsDomainsCreateOwnerContactIdErrorComponent
                | ApiV1DomainsDomainsCreatePlatformDnsRecordCreatedErrorComponent
                | ApiV1DomainsDomainsCreatePlatformServiceErrorComponent
                | ApiV1DomainsDomainsCreateProviderErrorComponent
                | ApiV1DomainsDomainsCreateProviderIdErrorComponent
                | ApiV1DomainsDomainsCreateProviderReferenceErrorComponent
                | ApiV1DomainsDomainsCreateProviderStatusErrorComponent
                | ApiV1DomainsDomainsCreateReconciliationEnabledErrorComponent
                | ApiV1DomainsDomainsCreateRegistrarDomainIdErrorComponent
                | ApiV1DomainsDomainsCreateRegistrarIdErrorComponent
                | ApiV1DomainsDomainsCreateRegistrarMetadataErrorComponent
                | ApiV1DomainsDomainsCreateRenewalModeErrorComponent
                | ApiV1DomainsDomainsCreateSlaAvailabilityErrorComponent
                | ApiV1DomainsDomainsCreateSlaTargetErrorComponent
                | ApiV1DomainsDomainsCreateSlaWindowDaysErrorComponent
                | ApiV1DomainsDomainsCreateSloAvailabilityErrorComponent
                | ApiV1DomainsDomainsCreateSloTargetErrorComponent
                | ApiV1DomainsDomainsCreateSloWindowDaysErrorComponent
                | ApiV1DomainsDomainsCreateTargetAvailabilityErrorComponent
                | ApiV1DomainsDomainsCreateTechContactIdErrorComponent
                | ApiV1DomainsDomainsCreateTolerationsErrorComponent
                | ApiV1DomainsDomainsCreateTransferLockErrorComponent
                | ApiV1DomainsDomainsCreateUsePlatformDnsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_0 = (
                        ApiV1DomainsDomainsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_1 = (
                        ApiV1DomainsDomainsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_2 = (
                        ApiV1DomainsDomainsCreateRegistrarIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_3 = (
                        ApiV1DomainsDomainsCreateDnsZoneIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_4 = (
                        ApiV1DomainsDomainsCreateUsePlatformDnsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_5 = (
                        ApiV1DomainsDomainsCreateOwnerContactIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_6 = (
                        ApiV1DomainsDomainsCreateAdminContactIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_7 = (
                        ApiV1DomainsDomainsCreateTechContactIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_8 = (
                        ApiV1DomainsDomainsCreateAuthCodeCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_9 = (
                        ApiV1DomainsDomainsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_10 = (
                        ApiV1DomainsDomainsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_11 = (
                        ApiV1DomainsDomainsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_12 = (
                        ApiV1DomainsDomainsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_13 = (
                        ApiV1DomainsDomainsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_14 = (
                        ApiV1DomainsDomainsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_15 = (
                        ApiV1DomainsDomainsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_16 = (
                        ApiV1DomainsDomainsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_17 = (
                        ApiV1DomainsDomainsCreateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_18 = (
                        ApiV1DomainsDomainsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_19 = (
                        ApiV1DomainsDomainsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_20 = (
                        ApiV1DomainsDomainsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_21 = (
                        ApiV1DomainsDomainsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_22 = (
                        ApiV1DomainsDomainsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_23 = (
                        ApiV1DomainsDomainsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_24 = (
                        ApiV1DomainsDomainsCreateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_25 = (
                        ApiV1DomainsDomainsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_26 = (
                        ApiV1DomainsDomainsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_27 = (
                        ApiV1DomainsDomainsCreateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_28 = (
                        ApiV1DomainsDomainsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_29 = (
                        ApiV1DomainsDomainsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_30 = (
                        ApiV1DomainsDomainsCreateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_31 = (
                        ApiV1DomainsDomainsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_32 = (
                        ApiV1DomainsDomainsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_33 = (
                        ApiV1DomainsDomainsCreateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_34 = (
                        ApiV1DomainsDomainsCreatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_35 = (
                        ApiV1DomainsDomainsCreateNameserversErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_36 = (
                        ApiV1DomainsDomainsCreateRenewalModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_37 = (
                        ApiV1DomainsDomainsCreateTransferLockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_38 = (
                        ApiV1DomainsDomainsCreateRegistrarDomainIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_39 = (
                        ApiV1DomainsDomainsCreateProviderStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_40 = (
                        ApiV1DomainsDomainsCreateExpiryDateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_41 = (
                        ApiV1DomainsDomainsCreateRegistrarMetadataErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_42 = (
                        ApiV1DomainsDomainsCreateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_43 = (
                        ApiV1DomainsDomainsCreateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_domains_domains_create_error_type_44 = (
                        ApiV1DomainsDomainsCreateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_domains_domains_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_domains_domains_create_error_type_45 = (
                    ApiV1DomainsDomainsCreateCreatedByUserErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_domains_domains_create_error_type_45

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_domains_domains_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_domains_domains_create_validation_error.additional_properties = d
        return api_v1_domains_domains_create_validation_error

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
