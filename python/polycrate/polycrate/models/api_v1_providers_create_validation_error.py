from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_providers_create_active_error_component import ApiV1ProvidersCreateActiveErrorComponent
    from ..models.api_v1_providers_create_address_error_component import ApiV1ProvidersCreateAddressErrorComponent
    from ..models.api_v1_providers_create_annotations_error_component import (
        ApiV1ProvidersCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_providers_create_archived_at_error_component import (
        ApiV1ProvidersCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_providers_create_archived_error_component import ApiV1ProvidersCreateArchivedErrorComponent
    from ..models.api_v1_providers_create_archived_reason_error_component import (
        ApiV1ProvidersCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_providers_create_asn_error_component import ApiV1ProvidersCreateAsnErrorComponent
    from ..models.api_v1_providers_create_ccm_block_error_component import ApiV1ProvidersCreateCcmBlockErrorComponent
    from ..models.api_v1_providers_create_certifications_error_component import (
        ApiV1ProvidersCreateCertificationsErrorComponent,
    )
    from ..models.api_v1_providers_create_criticality_error_component import (
        ApiV1ProvidersCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_providers_create_csi_controller_block_error_component import (
        ApiV1ProvidersCreateCsiControllerBlockErrorComponent,
    )
    from ..models.api_v1_providers_create_csi_storage_classes_error_component import (
        ApiV1ProvidersCreateCsiStorageClassesErrorComponent,
    )
    from ..models.api_v1_providers_create_debug_mode_error_component import ApiV1ProvidersCreateDebugModeErrorComponent
    from ..models.api_v1_providers_create_display_name_error_component import (
        ApiV1ProvidersCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_providers_create_emails_error_component import ApiV1ProvidersCreateEmailsErrorComponent
    from ..models.api_v1_providers_create_icon_content_type_error_component import (
        ApiV1ProvidersCreateIconContentTypeErrorComponent,
    )
    from ..models.api_v1_providers_create_icon_filename_error_component import (
        ApiV1ProvidersCreateIconFilenameErrorComponent,
    )
    from ..models.api_v1_providers_create_kind_error_component import ApiV1ProvidersCreateKindErrorComponent
    from ..models.api_v1_providers_create_labels_error_component import ApiV1ProvidersCreateLabelsErrorComponent
    from ..models.api_v1_providers_create_legal_name_error_component import ApiV1ProvidersCreateLegalNameErrorComponent
    from ..models.api_v1_providers_create_name_error_component import ApiV1ProvidersCreateNameErrorComponent
    from ..models.api_v1_providers_create_non_field_errors_error_component import (
        ApiV1ProvidersCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_providers_create_phone_error_component import ApiV1ProvidersCreatePhoneErrorComponent
    from ..models.api_v1_providers_create_platform_service_error_component import (
        ApiV1ProvidersCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_providers_create_provider_error_component import ApiV1ProvidersCreateProviderErrorComponent
    from ..models.api_v1_providers_create_provider_id_error_component import (
        ApiV1ProvidersCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_providers_create_provider_reference_error_component import (
        ApiV1ProvidersCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_providers_create_reconciliation_enabled_error_component import (
        ApiV1ProvidersCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_providers_create_sla_availability_error_component import (
        ApiV1ProvidersCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_create_sla_target_error_component import ApiV1ProvidersCreateSlaTargetErrorComponent
    from ..models.api_v1_providers_create_slo_availability_error_component import (
        ApiV1ProvidersCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_create_slo_target_error_component import ApiV1ProvidersCreateSloTargetErrorComponent
    from ..models.api_v1_providers_create_slug_error_component import ApiV1ProvidersCreateSlugErrorComponent
    from ..models.api_v1_providers_create_target_availability_error_component import (
        ApiV1ProvidersCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_providers_create_tolerations_error_component import (
        ApiV1ProvidersCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_providers_create_urls_error_component import ApiV1ProvidersCreateUrlsErrorComponent


T = TypeVar("T", bound="ApiV1ProvidersCreateValidationError")


@_attrs_define
class ApiV1ProvidersCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ProvidersCreateActiveErrorComponent | ApiV1ProvidersCreateAddressErrorComponent |
            ApiV1ProvidersCreateAnnotationsErrorComponent | ApiV1ProvidersCreateArchivedAtErrorComponent |
            ApiV1ProvidersCreateArchivedErrorComponent | ApiV1ProvidersCreateArchivedReasonErrorComponent |
            ApiV1ProvidersCreateAsnErrorComponent | ApiV1ProvidersCreateCcmBlockErrorComponent |
            ApiV1ProvidersCreateCertificationsErrorComponent | ApiV1ProvidersCreateCriticalityErrorComponent |
            ApiV1ProvidersCreateCsiControllerBlockErrorComponent | ApiV1ProvidersCreateCsiStorageClassesErrorComponent |
            ApiV1ProvidersCreateDebugModeErrorComponent | ApiV1ProvidersCreateDisplayNameErrorComponent |
            ApiV1ProvidersCreateEmailsErrorComponent | ApiV1ProvidersCreateIconContentTypeErrorComponent |
            ApiV1ProvidersCreateIconFilenameErrorComponent | ApiV1ProvidersCreateKindErrorComponent |
            ApiV1ProvidersCreateLabelsErrorComponent | ApiV1ProvidersCreateLegalNameErrorComponent |
            ApiV1ProvidersCreateNameErrorComponent | ApiV1ProvidersCreateNonFieldErrorsErrorComponent |
            ApiV1ProvidersCreatePhoneErrorComponent | ApiV1ProvidersCreatePlatformServiceErrorComponent |
            ApiV1ProvidersCreateProviderErrorComponent | ApiV1ProvidersCreateProviderIdErrorComponent |
            ApiV1ProvidersCreateProviderReferenceErrorComponent | ApiV1ProvidersCreateReconciliationEnabledErrorComponent |
            ApiV1ProvidersCreateSlaAvailabilityErrorComponent | ApiV1ProvidersCreateSlaTargetErrorComponent |
            ApiV1ProvidersCreateSloAvailabilityErrorComponent | ApiV1ProvidersCreateSloTargetErrorComponent |
            ApiV1ProvidersCreateSlugErrorComponent | ApiV1ProvidersCreateTargetAvailabilityErrorComponent |
            ApiV1ProvidersCreateTolerationsErrorComponent | ApiV1ProvidersCreateUrlsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ProvidersCreateActiveErrorComponent
        | ApiV1ProvidersCreateAddressErrorComponent
        | ApiV1ProvidersCreateAnnotationsErrorComponent
        | ApiV1ProvidersCreateArchivedAtErrorComponent
        | ApiV1ProvidersCreateArchivedErrorComponent
        | ApiV1ProvidersCreateArchivedReasonErrorComponent
        | ApiV1ProvidersCreateAsnErrorComponent
        | ApiV1ProvidersCreateCcmBlockErrorComponent
        | ApiV1ProvidersCreateCertificationsErrorComponent
        | ApiV1ProvidersCreateCriticalityErrorComponent
        | ApiV1ProvidersCreateCsiControllerBlockErrorComponent
        | ApiV1ProvidersCreateCsiStorageClassesErrorComponent
        | ApiV1ProvidersCreateDebugModeErrorComponent
        | ApiV1ProvidersCreateDisplayNameErrorComponent
        | ApiV1ProvidersCreateEmailsErrorComponent
        | ApiV1ProvidersCreateIconContentTypeErrorComponent
        | ApiV1ProvidersCreateIconFilenameErrorComponent
        | ApiV1ProvidersCreateKindErrorComponent
        | ApiV1ProvidersCreateLabelsErrorComponent
        | ApiV1ProvidersCreateLegalNameErrorComponent
        | ApiV1ProvidersCreateNameErrorComponent
        | ApiV1ProvidersCreateNonFieldErrorsErrorComponent
        | ApiV1ProvidersCreatePhoneErrorComponent
        | ApiV1ProvidersCreatePlatformServiceErrorComponent
        | ApiV1ProvidersCreateProviderErrorComponent
        | ApiV1ProvidersCreateProviderIdErrorComponent
        | ApiV1ProvidersCreateProviderReferenceErrorComponent
        | ApiV1ProvidersCreateReconciliationEnabledErrorComponent
        | ApiV1ProvidersCreateSlaAvailabilityErrorComponent
        | ApiV1ProvidersCreateSlaTargetErrorComponent
        | ApiV1ProvidersCreateSloAvailabilityErrorComponent
        | ApiV1ProvidersCreateSloTargetErrorComponent
        | ApiV1ProvidersCreateSlugErrorComponent
        | ApiV1ProvidersCreateTargetAvailabilityErrorComponent
        | ApiV1ProvidersCreateTolerationsErrorComponent
        | ApiV1ProvidersCreateUrlsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_providers_create_active_error_component import (
            ApiV1ProvidersCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_address_error_component import (
            ApiV1ProvidersCreateAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_annotations_error_component import (
            ApiV1ProvidersCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_archived_at_error_component import (
            ApiV1ProvidersCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_archived_error_component import (
            ApiV1ProvidersCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_archived_reason_error_component import (
            ApiV1ProvidersCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_asn_error_component import (
            ApiV1ProvidersCreateAsnErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_ccm_block_error_component import (
            ApiV1ProvidersCreateCcmBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_criticality_error_component import (
            ApiV1ProvidersCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_csi_controller_block_error_component import (
            ApiV1ProvidersCreateCsiControllerBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_csi_storage_classes_error_component import (
            ApiV1ProvidersCreateCsiStorageClassesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_debug_mode_error_component import (
            ApiV1ProvidersCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_display_name_error_component import (
            ApiV1ProvidersCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_emails_error_component import (
            ApiV1ProvidersCreateEmailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_icon_content_type_error_component import (
            ApiV1ProvidersCreateIconContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_icon_filename_error_component import (
            ApiV1ProvidersCreateIconFilenameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_kind_error_component import (
            ApiV1ProvidersCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_labels_error_component import (
            ApiV1ProvidersCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_legal_name_error_component import (
            ApiV1ProvidersCreateLegalNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_name_error_component import (
            ApiV1ProvidersCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_non_field_errors_error_component import (
            ApiV1ProvidersCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_phone_error_component import (
            ApiV1ProvidersCreatePhoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_platform_service_error_component import (
            ApiV1ProvidersCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_provider_error_component import (
            ApiV1ProvidersCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_provider_id_error_component import (
            ApiV1ProvidersCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_provider_reference_error_component import (
            ApiV1ProvidersCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_reconciliation_enabled_error_component import (
            ApiV1ProvidersCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_sla_availability_error_component import (
            ApiV1ProvidersCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_sla_target_error_component import (
            ApiV1ProvidersCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_slo_availability_error_component import (
            ApiV1ProvidersCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_slo_target_error_component import (
            ApiV1ProvidersCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_slug_error_component import (
            ApiV1ProvidersCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_target_availability_error_component import (
            ApiV1ProvidersCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_tolerations_error_component import (
            ApiV1ProvidersCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_urls_error_component import (
            ApiV1ProvidersCreateUrlsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ProvidersCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateLegalNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateSlugErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateIconContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateIconFilenameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateCcmBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateCsiControllerBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateCsiStorageClassesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateEmailsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreatePhoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateAsnErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ProvidersCreateUrlsErrorComponent):
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
        from ..models.api_v1_providers_create_active_error_component import (
            ApiV1ProvidersCreateActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_address_error_component import (
            ApiV1ProvidersCreateAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_annotations_error_component import (
            ApiV1ProvidersCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_archived_at_error_component import (
            ApiV1ProvidersCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_archived_error_component import (
            ApiV1ProvidersCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_archived_reason_error_component import (
            ApiV1ProvidersCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_asn_error_component import (
            ApiV1ProvidersCreateAsnErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_ccm_block_error_component import (
            ApiV1ProvidersCreateCcmBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_certifications_error_component import (
            ApiV1ProvidersCreateCertificationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_criticality_error_component import (
            ApiV1ProvidersCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_csi_controller_block_error_component import (
            ApiV1ProvidersCreateCsiControllerBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_csi_storage_classes_error_component import (
            ApiV1ProvidersCreateCsiStorageClassesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_debug_mode_error_component import (
            ApiV1ProvidersCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_display_name_error_component import (
            ApiV1ProvidersCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_emails_error_component import (
            ApiV1ProvidersCreateEmailsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_icon_content_type_error_component import (
            ApiV1ProvidersCreateIconContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_icon_filename_error_component import (
            ApiV1ProvidersCreateIconFilenameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_kind_error_component import (
            ApiV1ProvidersCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_labels_error_component import (
            ApiV1ProvidersCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_legal_name_error_component import (
            ApiV1ProvidersCreateLegalNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_name_error_component import (
            ApiV1ProvidersCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_non_field_errors_error_component import (
            ApiV1ProvidersCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_phone_error_component import (
            ApiV1ProvidersCreatePhoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_platform_service_error_component import (
            ApiV1ProvidersCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_provider_error_component import (
            ApiV1ProvidersCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_provider_id_error_component import (
            ApiV1ProvidersCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_provider_reference_error_component import (
            ApiV1ProvidersCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_reconciliation_enabled_error_component import (
            ApiV1ProvidersCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_sla_availability_error_component import (
            ApiV1ProvidersCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_sla_target_error_component import (
            ApiV1ProvidersCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_slo_availability_error_component import (
            ApiV1ProvidersCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_slo_target_error_component import (
            ApiV1ProvidersCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_slug_error_component import (
            ApiV1ProvidersCreateSlugErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_target_availability_error_component import (
            ApiV1ProvidersCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_tolerations_error_component import (
            ApiV1ProvidersCreateTolerationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_providers_create_urls_error_component import (
            ApiV1ProvidersCreateUrlsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ProvidersCreateActiveErrorComponent
                | ApiV1ProvidersCreateAddressErrorComponent
                | ApiV1ProvidersCreateAnnotationsErrorComponent
                | ApiV1ProvidersCreateArchivedAtErrorComponent
                | ApiV1ProvidersCreateArchivedErrorComponent
                | ApiV1ProvidersCreateArchivedReasonErrorComponent
                | ApiV1ProvidersCreateAsnErrorComponent
                | ApiV1ProvidersCreateCcmBlockErrorComponent
                | ApiV1ProvidersCreateCertificationsErrorComponent
                | ApiV1ProvidersCreateCriticalityErrorComponent
                | ApiV1ProvidersCreateCsiControllerBlockErrorComponent
                | ApiV1ProvidersCreateCsiStorageClassesErrorComponent
                | ApiV1ProvidersCreateDebugModeErrorComponent
                | ApiV1ProvidersCreateDisplayNameErrorComponent
                | ApiV1ProvidersCreateEmailsErrorComponent
                | ApiV1ProvidersCreateIconContentTypeErrorComponent
                | ApiV1ProvidersCreateIconFilenameErrorComponent
                | ApiV1ProvidersCreateKindErrorComponent
                | ApiV1ProvidersCreateLabelsErrorComponent
                | ApiV1ProvidersCreateLegalNameErrorComponent
                | ApiV1ProvidersCreateNameErrorComponent
                | ApiV1ProvidersCreateNonFieldErrorsErrorComponent
                | ApiV1ProvidersCreatePhoneErrorComponent
                | ApiV1ProvidersCreatePlatformServiceErrorComponent
                | ApiV1ProvidersCreateProviderErrorComponent
                | ApiV1ProvidersCreateProviderIdErrorComponent
                | ApiV1ProvidersCreateProviderReferenceErrorComponent
                | ApiV1ProvidersCreateReconciliationEnabledErrorComponent
                | ApiV1ProvidersCreateSlaAvailabilityErrorComponent
                | ApiV1ProvidersCreateSlaTargetErrorComponent
                | ApiV1ProvidersCreateSloAvailabilityErrorComponent
                | ApiV1ProvidersCreateSloTargetErrorComponent
                | ApiV1ProvidersCreateSlugErrorComponent
                | ApiV1ProvidersCreateTargetAvailabilityErrorComponent
                | ApiV1ProvidersCreateTolerationsErrorComponent
                | ApiV1ProvidersCreateUrlsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_0 = (
                        ApiV1ProvidersCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_1 = (
                        ApiV1ProvidersCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_2 = (
                        ApiV1ProvidersCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_3 = (
                        ApiV1ProvidersCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_4 = (
                        ApiV1ProvidersCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_5 = (
                        ApiV1ProvidersCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_6 = (
                        ApiV1ProvidersCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_7 = (
                        ApiV1ProvidersCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_8 = (
                        ApiV1ProvidersCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_9 = (
                        ApiV1ProvidersCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_10 = (
                        ApiV1ProvidersCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_11 = (
                        ApiV1ProvidersCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_12 = (
                        ApiV1ProvidersCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_13 = (
                        ApiV1ProvidersCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_14 = (
                        ApiV1ProvidersCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_15 = (
                        ApiV1ProvidersCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_16 = (
                        ApiV1ProvidersCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_17 = (
                        ApiV1ProvidersCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_18 = (
                        ApiV1ProvidersCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_19 = (
                        ApiV1ProvidersCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_20 = (
                        ApiV1ProvidersCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_21 = (
                        ApiV1ProvidersCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_22 = (
                        ApiV1ProvidersCreateLegalNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_23 = (
                        ApiV1ProvidersCreateSlugErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_24 = (
                        ApiV1ProvidersCreateActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_25 = (
                        ApiV1ProvidersCreateIconContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_26 = (
                        ApiV1ProvidersCreateIconFilenameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_27 = (
                        ApiV1ProvidersCreateCcmBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_28 = (
                        ApiV1ProvidersCreateCsiControllerBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_29 = (
                        ApiV1ProvidersCreateCsiStorageClassesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_30 = (
                        ApiV1ProvidersCreateAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_31 = (
                        ApiV1ProvidersCreateEmailsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_32 = (
                        ApiV1ProvidersCreatePhoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_33 = (
                        ApiV1ProvidersCreateAsnErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_providers_create_error_type_34 = (
                        ApiV1ProvidersCreateUrlsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_providers_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_providers_create_error_type_35 = (
                    ApiV1ProvidersCreateCertificationsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_providers_create_error_type_35

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_providers_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_providers_create_validation_error.additional_properties = d
        return api_v1_providers_create_validation_error

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
