from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_providers_reconcile_create_active_error_component import (
        ApiV1ProvidersReconcileCreateActiveErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_address_error_component import (
        ApiV1ProvidersReconcileCreateAddressErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_annotations_error_component import (
        ApiV1ProvidersReconcileCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_archived_at_error_component import (
        ApiV1ProvidersReconcileCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_archived_error_component import (
        ApiV1ProvidersReconcileCreateArchivedErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_archived_reason_error_component import (
        ApiV1ProvidersReconcileCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_asn_error_component import (
        ApiV1ProvidersReconcileCreateAsnErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_ccm_block_error_component import (
        ApiV1ProvidersReconcileCreateCcmBlockErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_certifications_error_component import (
        ApiV1ProvidersReconcileCreateCertificationsErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_criticality_error_component import (
        ApiV1ProvidersReconcileCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_csi_controller_block_error_component import (
        ApiV1ProvidersReconcileCreateCsiControllerBlockErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_csi_storage_classes_error_component import (
        ApiV1ProvidersReconcileCreateCsiStorageClassesErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_debug_mode_error_component import (
        ApiV1ProvidersReconcileCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_display_name_error_component import (
        ApiV1ProvidersReconcileCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_emails_error_component import (
        ApiV1ProvidersReconcileCreateEmailsErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_icon_content_type_error_component import (
        ApiV1ProvidersReconcileCreateIconContentTypeErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_icon_filename_error_component import (
        ApiV1ProvidersReconcileCreateIconFilenameErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_kind_error_component import (
        ApiV1ProvidersReconcileCreateKindErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_labels_error_component import (
        ApiV1ProvidersReconcileCreateLabelsErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_legal_name_error_component import (
        ApiV1ProvidersReconcileCreateLegalNameErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_name_error_component import (
        ApiV1ProvidersReconcileCreateNameErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_non_field_errors_error_component import (
        ApiV1ProvidersReconcileCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_phone_error_component import (
        ApiV1ProvidersReconcileCreatePhoneErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_platform_service_error_component import (
        ApiV1ProvidersReconcileCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_provider_error_component import (
        ApiV1ProvidersReconcileCreateProviderErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_provider_id_error_component import (
        ApiV1ProvidersReconcileCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_provider_reference_error_component import (
        ApiV1ProvidersReconcileCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_reconciliation_enabled_error_component import (
        ApiV1ProvidersReconcileCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_sla_availability_error_component import (
        ApiV1ProvidersReconcileCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_sla_target_error_component import (
        ApiV1ProvidersReconcileCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_slo_availability_error_component import (
        ApiV1ProvidersReconcileCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_slo_target_error_component import (
        ApiV1ProvidersReconcileCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_slug_error_component import (
        ApiV1ProvidersReconcileCreateSlugErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_target_availability_error_component import (
        ApiV1ProvidersReconcileCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_tolerations_error_component import (
        ApiV1ProvidersReconcileCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_providers_reconcile_create_urls_error_component import (
        ApiV1ProvidersReconcileCreateUrlsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ProvidersReconcileCreateValidationError")


@_attrs_define
class ApiV1ProvidersReconcileCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProvidersReconcileCreateActiveErrorComponent |
            ApiV1ProvidersReconcileCreateAddressErrorComponent | ApiV1ProvidersReconcileCreateAnnotationsErrorComponent |
            ApiV1ProvidersReconcileCreateArchivedAtErrorComponent | ApiV1ProvidersReconcileCreateArchivedErrorComponent |
            ApiV1ProvidersReconcileCreateArchivedReasonErrorComponent | ApiV1ProvidersReconcileCreateAsnErrorComponent |
            ApiV1ProvidersReconcileCreateCcmBlockErrorComponent | ApiV1ProvidersReconcileCreateCertificationsErrorComponent
            | ApiV1ProvidersReconcileCreateCriticalityErrorComponent |
            ApiV1ProvidersReconcileCreateCsiControllerBlockErrorComponent |
            ApiV1ProvidersReconcileCreateCsiStorageClassesErrorComponent |
            ApiV1ProvidersReconcileCreateDebugModeErrorComponent | ApiV1ProvidersReconcileCreateDisplayNameErrorComponent |
            ApiV1ProvidersReconcileCreateEmailsErrorComponent | ApiV1ProvidersReconcileCreateIconContentTypeErrorComponent |
            ApiV1ProvidersReconcileCreateIconFilenameErrorComponent | ApiV1ProvidersReconcileCreateKindErrorComponent |
            ApiV1ProvidersReconcileCreateLabelsErrorComponent | ApiV1ProvidersReconcileCreateLegalNameErrorComponent |
            ApiV1ProvidersReconcileCreateNameErrorComponent | ApiV1ProvidersReconcileCreateNonFieldErrorsErrorComponent |
            ApiV1ProvidersReconcileCreatePhoneErrorComponent | ApiV1ProvidersReconcileCreatePlatformServiceErrorComponent |
            ApiV1ProvidersReconcileCreateProviderErrorComponent | ApiV1ProvidersReconcileCreateProviderIdErrorComponent |
            ApiV1ProvidersReconcileCreateProviderReferenceErrorComponent |
            ApiV1ProvidersReconcileCreateReconciliationEnabledErrorComponent |
            ApiV1ProvidersReconcileCreateSlaAvailabilityErrorComponent |
            ApiV1ProvidersReconcileCreateSlaTargetErrorComponent |
            ApiV1ProvidersReconcileCreateSloAvailabilityErrorComponent |
            ApiV1ProvidersReconcileCreateSloTargetErrorComponent | ApiV1ProvidersReconcileCreateSlugErrorComponent |
            ApiV1ProvidersReconcileCreateTargetAvailabilityErrorComponent |
            ApiV1ProvidersReconcileCreateTolerationsErrorComponent | ApiV1ProvidersReconcileCreateUrlsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProvidersReconcileCreateActiveErrorComponent
        | ApiV1ProvidersReconcileCreateAddressErrorComponent
        | ApiV1ProvidersReconcileCreateAnnotationsErrorComponent
        | ApiV1ProvidersReconcileCreateArchivedAtErrorComponent
        | ApiV1ProvidersReconcileCreateArchivedErrorComponent
        | ApiV1ProvidersReconcileCreateArchivedReasonErrorComponent
        | ApiV1ProvidersReconcileCreateAsnErrorComponent
        | ApiV1ProvidersReconcileCreateCcmBlockErrorComponent
        | ApiV1ProvidersReconcileCreateCertificationsErrorComponent
        | ApiV1ProvidersReconcileCreateCriticalityErrorComponent
        | ApiV1ProvidersReconcileCreateCsiControllerBlockErrorComponent
        | ApiV1ProvidersReconcileCreateCsiStorageClassesErrorComponent
        | ApiV1ProvidersReconcileCreateDebugModeErrorComponent
        | ApiV1ProvidersReconcileCreateDisplayNameErrorComponent
        | ApiV1ProvidersReconcileCreateEmailsErrorComponent
        | ApiV1ProvidersReconcileCreateIconContentTypeErrorComponent
        | ApiV1ProvidersReconcileCreateIconFilenameErrorComponent
        | ApiV1ProvidersReconcileCreateKindErrorComponent
        | ApiV1ProvidersReconcileCreateLabelsErrorComponent
        | ApiV1ProvidersReconcileCreateLegalNameErrorComponent
        | ApiV1ProvidersReconcileCreateNameErrorComponent
        | ApiV1ProvidersReconcileCreateNonFieldErrorsErrorComponent
        | ApiV1ProvidersReconcileCreatePhoneErrorComponent
        | ApiV1ProvidersReconcileCreatePlatformServiceErrorComponent
        | ApiV1ProvidersReconcileCreateProviderErrorComponent
        | ApiV1ProvidersReconcileCreateProviderIdErrorComponent
        | ApiV1ProvidersReconcileCreateProviderReferenceErrorComponent
        | ApiV1ProvidersReconcileCreateReconciliationEnabledErrorComponent
        | ApiV1ProvidersReconcileCreateSlaAvailabilityErrorComponent
        | ApiV1ProvidersReconcileCreateSlaTargetErrorComponent
        | ApiV1ProvidersReconcileCreateSloAvailabilityErrorComponent
        | ApiV1ProvidersReconcileCreateSloTargetErrorComponent
        | ApiV1ProvidersReconcileCreateSlugErrorComponent
        | ApiV1ProvidersReconcileCreateTargetAvailabilityErrorComponent
        | ApiV1ProvidersReconcileCreateTolerationsErrorComponent
        | ApiV1ProvidersReconcileCreateUrlsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_providers_reconcile_create_active_error_component import (
            ApiV1ProvidersReconcileCreateActiveErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_address_error_component import (
            ApiV1ProvidersReconcileCreateAddressErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_annotations_error_component import (
            ApiV1ProvidersReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_archived_at_error_component import (
            ApiV1ProvidersReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_archived_error_component import (
            ApiV1ProvidersReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_archived_reason_error_component import (
            ApiV1ProvidersReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_asn_error_component import (
            ApiV1ProvidersReconcileCreateAsnErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_ccm_block_error_component import (
            ApiV1ProvidersReconcileCreateCcmBlockErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_criticality_error_component import (
            ApiV1ProvidersReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_csi_controller_block_error_component import (
            ApiV1ProvidersReconcileCreateCsiControllerBlockErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_csi_storage_classes_error_component import (
            ApiV1ProvidersReconcileCreateCsiStorageClassesErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_debug_mode_error_component import (
            ApiV1ProvidersReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_display_name_error_component import (
            ApiV1ProvidersReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_emails_error_component import (
            ApiV1ProvidersReconcileCreateEmailsErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_icon_content_type_error_component import (
            ApiV1ProvidersReconcileCreateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_icon_filename_error_component import (
            ApiV1ProvidersReconcileCreateIconFilenameErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_kind_error_component import (
            ApiV1ProvidersReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_labels_error_component import (
            ApiV1ProvidersReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_legal_name_error_component import (
            ApiV1ProvidersReconcileCreateLegalNameErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_name_error_component import (
            ApiV1ProvidersReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_non_field_errors_error_component import (
            ApiV1ProvidersReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_phone_error_component import (
            ApiV1ProvidersReconcileCreatePhoneErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_platform_service_error_component import (
            ApiV1ProvidersReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_provider_error_component import (
            ApiV1ProvidersReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_provider_id_error_component import (
            ApiV1ProvidersReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_provider_reference_error_component import (
            ApiV1ProvidersReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1ProvidersReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_sla_availability_error_component import (
            ApiV1ProvidersReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_sla_target_error_component import (
            ApiV1ProvidersReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_slo_availability_error_component import (
            ApiV1ProvidersReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_slo_target_error_component import (
            ApiV1ProvidersReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_slug_error_component import (
            ApiV1ProvidersReconcileCreateSlugErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_target_availability_error_component import (
            ApiV1ProvidersReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_tolerations_error_component import (
            ApiV1ProvidersReconcileCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_urls_error_component import (
            ApiV1ProvidersReconcileCreateUrlsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProvidersReconcileCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateLegalNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateIconContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateIconFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateCcmBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateCsiControllerBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateCsiStorageClassesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateEmailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreatePhoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateAsnErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersReconcileCreateUrlsErrorComponent):
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
        from ..models.api_v1_providers_reconcile_create_active_error_component import (
            ApiV1ProvidersReconcileCreateActiveErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_address_error_component import (
            ApiV1ProvidersReconcileCreateAddressErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_annotations_error_component import (
            ApiV1ProvidersReconcileCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_archived_at_error_component import (
            ApiV1ProvidersReconcileCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_archived_error_component import (
            ApiV1ProvidersReconcileCreateArchivedErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_archived_reason_error_component import (
            ApiV1ProvidersReconcileCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_asn_error_component import (
            ApiV1ProvidersReconcileCreateAsnErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_ccm_block_error_component import (
            ApiV1ProvidersReconcileCreateCcmBlockErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_certifications_error_component import (
            ApiV1ProvidersReconcileCreateCertificationsErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_criticality_error_component import (
            ApiV1ProvidersReconcileCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_csi_controller_block_error_component import (
            ApiV1ProvidersReconcileCreateCsiControllerBlockErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_csi_storage_classes_error_component import (
            ApiV1ProvidersReconcileCreateCsiStorageClassesErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_debug_mode_error_component import (
            ApiV1ProvidersReconcileCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_display_name_error_component import (
            ApiV1ProvidersReconcileCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_emails_error_component import (
            ApiV1ProvidersReconcileCreateEmailsErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_icon_content_type_error_component import (
            ApiV1ProvidersReconcileCreateIconContentTypeErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_icon_filename_error_component import (
            ApiV1ProvidersReconcileCreateIconFilenameErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_kind_error_component import (
            ApiV1ProvidersReconcileCreateKindErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_labels_error_component import (
            ApiV1ProvidersReconcileCreateLabelsErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_legal_name_error_component import (
            ApiV1ProvidersReconcileCreateLegalNameErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_name_error_component import (
            ApiV1ProvidersReconcileCreateNameErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_non_field_errors_error_component import (
            ApiV1ProvidersReconcileCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_phone_error_component import (
            ApiV1ProvidersReconcileCreatePhoneErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_platform_service_error_component import (
            ApiV1ProvidersReconcileCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_provider_error_component import (
            ApiV1ProvidersReconcileCreateProviderErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_provider_id_error_component import (
            ApiV1ProvidersReconcileCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_provider_reference_error_component import (
            ApiV1ProvidersReconcileCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1ProvidersReconcileCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_sla_availability_error_component import (
            ApiV1ProvidersReconcileCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_sla_target_error_component import (
            ApiV1ProvidersReconcileCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_slo_availability_error_component import (
            ApiV1ProvidersReconcileCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_slo_target_error_component import (
            ApiV1ProvidersReconcileCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_slug_error_component import (
            ApiV1ProvidersReconcileCreateSlugErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_target_availability_error_component import (
            ApiV1ProvidersReconcileCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_tolerations_error_component import (
            ApiV1ProvidersReconcileCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_providers_reconcile_create_urls_error_component import (
            ApiV1ProvidersReconcileCreateUrlsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProvidersReconcileCreateActiveErrorComponent
                | ApiV1ProvidersReconcileCreateAddressErrorComponent
                | ApiV1ProvidersReconcileCreateAnnotationsErrorComponent
                | ApiV1ProvidersReconcileCreateArchivedAtErrorComponent
                | ApiV1ProvidersReconcileCreateArchivedErrorComponent
                | ApiV1ProvidersReconcileCreateArchivedReasonErrorComponent
                | ApiV1ProvidersReconcileCreateAsnErrorComponent
                | ApiV1ProvidersReconcileCreateCcmBlockErrorComponent
                | ApiV1ProvidersReconcileCreateCertificationsErrorComponent
                | ApiV1ProvidersReconcileCreateCriticalityErrorComponent
                | ApiV1ProvidersReconcileCreateCsiControllerBlockErrorComponent
                | ApiV1ProvidersReconcileCreateCsiStorageClassesErrorComponent
                | ApiV1ProvidersReconcileCreateDebugModeErrorComponent
                | ApiV1ProvidersReconcileCreateDisplayNameErrorComponent
                | ApiV1ProvidersReconcileCreateEmailsErrorComponent
                | ApiV1ProvidersReconcileCreateIconContentTypeErrorComponent
                | ApiV1ProvidersReconcileCreateIconFilenameErrorComponent
                | ApiV1ProvidersReconcileCreateKindErrorComponent
                | ApiV1ProvidersReconcileCreateLabelsErrorComponent
                | ApiV1ProvidersReconcileCreateLegalNameErrorComponent
                | ApiV1ProvidersReconcileCreateNameErrorComponent
                | ApiV1ProvidersReconcileCreateNonFieldErrorsErrorComponent
                | ApiV1ProvidersReconcileCreatePhoneErrorComponent
                | ApiV1ProvidersReconcileCreatePlatformServiceErrorComponent
                | ApiV1ProvidersReconcileCreateProviderErrorComponent
                | ApiV1ProvidersReconcileCreateProviderIdErrorComponent
                | ApiV1ProvidersReconcileCreateProviderReferenceErrorComponent
                | ApiV1ProvidersReconcileCreateReconciliationEnabledErrorComponent
                | ApiV1ProvidersReconcileCreateSlaAvailabilityErrorComponent
                | ApiV1ProvidersReconcileCreateSlaTargetErrorComponent
                | ApiV1ProvidersReconcileCreateSloAvailabilityErrorComponent
                | ApiV1ProvidersReconcileCreateSloTargetErrorComponent
                | ApiV1ProvidersReconcileCreateSlugErrorComponent
                | ApiV1ProvidersReconcileCreateTargetAvailabilityErrorComponent
                | ApiV1ProvidersReconcileCreateTolerationsErrorComponent
                | ApiV1ProvidersReconcileCreateUrlsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_0 = (
                        ApiV1ProvidersReconcileCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_1 = (
                        ApiV1ProvidersReconcileCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_2 = (
                        ApiV1ProvidersReconcileCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_3 = (
                        ApiV1ProvidersReconcileCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_4 = (
                        ApiV1ProvidersReconcileCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_5 = (
                        ApiV1ProvidersReconcileCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_6 = (
                        ApiV1ProvidersReconcileCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_7 = (
                        ApiV1ProvidersReconcileCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_8 = (
                        ApiV1ProvidersReconcileCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_9 = (
                        ApiV1ProvidersReconcileCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_10 = (
                        ApiV1ProvidersReconcileCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_11 = (
                        ApiV1ProvidersReconcileCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_12 = (
                        ApiV1ProvidersReconcileCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_13 = (
                        ApiV1ProvidersReconcileCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_14 = (
                        ApiV1ProvidersReconcileCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_15 = (
                        ApiV1ProvidersReconcileCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_16 = (
                        ApiV1ProvidersReconcileCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_17 = (
                        ApiV1ProvidersReconcileCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_18 = (
                        ApiV1ProvidersReconcileCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_19 = (
                        ApiV1ProvidersReconcileCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_20 = (
                        ApiV1ProvidersReconcileCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_21 = (
                        ApiV1ProvidersReconcileCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_22 = (
                        ApiV1ProvidersReconcileCreateLegalNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_23 = (
                        ApiV1ProvidersReconcileCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_24 = (
                        ApiV1ProvidersReconcileCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_25 = (
                        ApiV1ProvidersReconcileCreateIconContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_26 = (
                        ApiV1ProvidersReconcileCreateIconFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_27 = (
                        ApiV1ProvidersReconcileCreateCcmBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_28 = (
                        ApiV1ProvidersReconcileCreateCsiControllerBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_29 = (
                        ApiV1ProvidersReconcileCreateCsiStorageClassesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_30 = (
                        ApiV1ProvidersReconcileCreateAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_31 = (
                        ApiV1ProvidersReconcileCreateEmailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_32 = (
                        ApiV1ProvidersReconcileCreatePhoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_33 = (
                        ApiV1ProvidersReconcileCreateAsnErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_reconcile_create_error_type_34 = (
                        ApiV1ProvidersReconcileCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_reconcile_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_providers_reconcile_create_error_type_35 = (
                    ApiV1ProvidersReconcileCreateCertificationsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_providers_reconcile_create_error_type_35

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_providers_reconcile_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_providers_reconcile_create_validation_error.additional_properties = d
        return api_v1_providers_reconcile_create_validation_error

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
