from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_organization_products_update_active_from_error_component import (
        ApiV1PricingOrganizationProductsUpdateActiveFromErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_active_until_error_component import (
        ApiV1PricingOrganizationProductsUpdateActiveUntilErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_agreed_price_error_component import (
        ApiV1PricingOrganizationProductsUpdateAgreedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_agreed_price_reason_error_component import (
        ApiV1PricingOrganizationProductsUpdateAgreedPriceReasonErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_annotations_error_component import (
        ApiV1PricingOrganizationProductsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_archived_at_error_component import (
        ApiV1PricingOrganizationProductsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_archived_error_component import (
        ApiV1PricingOrganizationProductsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_archived_reason_error_component import (
        ApiV1PricingOrganizationProductsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_auto_managed_error_component import (
        ApiV1PricingOrganizationProductsUpdateAutoManagedErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_catalogue_app_error_component import (
        ApiV1PricingOrganizationProductsUpdateCatalogueAppErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_content_type_error_component import (
        ApiV1PricingOrganizationProductsUpdateContentTypeErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_criticality_error_component import (
        ApiV1PricingOrganizationProductsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_debug_mode_error_component import (
        ApiV1PricingOrganizationProductsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_display_name_error_component import (
        ApiV1PricingOrganizationProductsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_internal_note_error_component import (
        ApiV1PricingOrganizationProductsUpdateInternalNoteErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_kind_error_component import (
        ApiV1PricingOrganizationProductsUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_labels_error_component import (
        ApiV1PricingOrganizationProductsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_name_error_component import (
        ApiV1PricingOrganizationProductsUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_non_field_errors_error_component import (
        ApiV1PricingOrganizationProductsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_object_id_error_component import (
        ApiV1PricingOrganizationProductsUpdateObjectIdErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_platform_service_error_component import (
        ApiV1PricingOrganizationProductsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_provider_error_component import (
        ApiV1PricingOrganizationProductsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_provider_id_error_component import (
        ApiV1PricingOrganizationProductsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_provider_reference_error_component import (
        ApiV1PricingOrganizationProductsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_reconciliation_enabled_error_component import (
        ApiV1PricingOrganizationProductsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_sla_availability_error_component import (
        ApiV1PricingOrganizationProductsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_sla_target_error_component import (
        ApiV1PricingOrganizationProductsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_slo_availability_error_component import (
        ApiV1PricingOrganizationProductsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_slo_target_error_component import (
        ApiV1PricingOrganizationProductsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_target_availability_error_component import (
        ApiV1PricingOrganizationProductsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_organization_products_update_tolerations_error_component import (
        ApiV1PricingOrganizationProductsUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingOrganizationProductsUpdateValidationError")


@_attrs_define
class ApiV1PricingOrganizationProductsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingOrganizationProductsUpdateActiveFromErrorComponent |
            ApiV1PricingOrganizationProductsUpdateActiveUntilErrorComponent |
            ApiV1PricingOrganizationProductsUpdateAgreedPriceErrorComponent |
            ApiV1PricingOrganizationProductsUpdateAgreedPriceReasonErrorComponent |
            ApiV1PricingOrganizationProductsUpdateAnnotationsErrorComponent |
            ApiV1PricingOrganizationProductsUpdateArchivedAtErrorComponent |
            ApiV1PricingOrganizationProductsUpdateArchivedErrorComponent |
            ApiV1PricingOrganizationProductsUpdateArchivedReasonErrorComponent |
            ApiV1PricingOrganizationProductsUpdateAutoManagedErrorComponent |
            ApiV1PricingOrganizationProductsUpdateCatalogueAppErrorComponent |
            ApiV1PricingOrganizationProductsUpdateContentTypeErrorComponent |
            ApiV1PricingOrganizationProductsUpdateCriticalityErrorComponent |
            ApiV1PricingOrganizationProductsUpdateDebugModeErrorComponent |
            ApiV1PricingOrganizationProductsUpdateDisplayNameErrorComponent |
            ApiV1PricingOrganizationProductsUpdateInternalNoteErrorComponent |
            ApiV1PricingOrganizationProductsUpdateKindErrorComponent |
            ApiV1PricingOrganizationProductsUpdateLabelsErrorComponent |
            ApiV1PricingOrganizationProductsUpdateNameErrorComponent |
            ApiV1PricingOrganizationProductsUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingOrganizationProductsUpdateObjectIdErrorComponent |
            ApiV1PricingOrganizationProductsUpdatePlatformServiceErrorComponent |
            ApiV1PricingOrganizationProductsUpdateProviderErrorComponent |
            ApiV1PricingOrganizationProductsUpdateProviderIdErrorComponent |
            ApiV1PricingOrganizationProductsUpdateProviderReferenceErrorComponent |
            ApiV1PricingOrganizationProductsUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingOrganizationProductsUpdateSlaAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsUpdateSlaTargetErrorComponent |
            ApiV1PricingOrganizationProductsUpdateSloAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsUpdateSloTargetErrorComponent |
            ApiV1PricingOrganizationProductsUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingOrganizationProductsUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingOrganizationProductsUpdateActiveFromErrorComponent
        | ApiV1PricingOrganizationProductsUpdateActiveUntilErrorComponent
        | ApiV1PricingOrganizationProductsUpdateAgreedPriceErrorComponent
        | ApiV1PricingOrganizationProductsUpdateAgreedPriceReasonErrorComponent
        | ApiV1PricingOrganizationProductsUpdateAnnotationsErrorComponent
        | ApiV1PricingOrganizationProductsUpdateArchivedAtErrorComponent
        | ApiV1PricingOrganizationProductsUpdateArchivedErrorComponent
        | ApiV1PricingOrganizationProductsUpdateArchivedReasonErrorComponent
        | ApiV1PricingOrganizationProductsUpdateAutoManagedErrorComponent
        | ApiV1PricingOrganizationProductsUpdateCatalogueAppErrorComponent
        | ApiV1PricingOrganizationProductsUpdateContentTypeErrorComponent
        | ApiV1PricingOrganizationProductsUpdateCriticalityErrorComponent
        | ApiV1PricingOrganizationProductsUpdateDebugModeErrorComponent
        | ApiV1PricingOrganizationProductsUpdateDisplayNameErrorComponent
        | ApiV1PricingOrganizationProductsUpdateInternalNoteErrorComponent
        | ApiV1PricingOrganizationProductsUpdateKindErrorComponent
        | ApiV1PricingOrganizationProductsUpdateLabelsErrorComponent
        | ApiV1PricingOrganizationProductsUpdateNameErrorComponent
        | ApiV1PricingOrganizationProductsUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingOrganizationProductsUpdateObjectIdErrorComponent
        | ApiV1PricingOrganizationProductsUpdatePlatformServiceErrorComponent
        | ApiV1PricingOrganizationProductsUpdateProviderErrorComponent
        | ApiV1PricingOrganizationProductsUpdateProviderIdErrorComponent
        | ApiV1PricingOrganizationProductsUpdateProviderReferenceErrorComponent
        | ApiV1PricingOrganizationProductsUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingOrganizationProductsUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsUpdateSlaTargetErrorComponent
        | ApiV1PricingOrganizationProductsUpdateSloAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsUpdateSloTargetErrorComponent
        | ApiV1PricingOrganizationProductsUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingOrganizationProductsUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_organization_products_update_active_from_error_component import (
            ApiV1PricingOrganizationProductsUpdateActiveFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_active_until_error_component import (
            ApiV1PricingOrganizationProductsUpdateActiveUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_agreed_price_error_component import (
            ApiV1PricingOrganizationProductsUpdateAgreedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_agreed_price_reason_error_component import (
            ApiV1PricingOrganizationProductsUpdateAgreedPriceReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_annotations_error_component import (
            ApiV1PricingOrganizationProductsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_archived_at_error_component import (
            ApiV1PricingOrganizationProductsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_archived_error_component import (
            ApiV1PricingOrganizationProductsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_archived_reason_error_component import (
            ApiV1PricingOrganizationProductsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_auto_managed_error_component import (
            ApiV1PricingOrganizationProductsUpdateAutoManagedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_catalogue_app_error_component import (
            ApiV1PricingOrganizationProductsUpdateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_content_type_error_component import (
            ApiV1PricingOrganizationProductsUpdateContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_criticality_error_component import (
            ApiV1PricingOrganizationProductsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_debug_mode_error_component import (
            ApiV1PricingOrganizationProductsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_display_name_error_component import (
            ApiV1PricingOrganizationProductsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_kind_error_component import (
            ApiV1PricingOrganizationProductsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_labels_error_component import (
            ApiV1PricingOrganizationProductsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_name_error_component import (
            ApiV1PricingOrganizationProductsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_non_field_errors_error_component import (
            ApiV1PricingOrganizationProductsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_object_id_error_component import (
            ApiV1PricingOrganizationProductsUpdateObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_platform_service_error_component import (
            ApiV1PricingOrganizationProductsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_provider_error_component import (
            ApiV1PricingOrganizationProductsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_provider_id_error_component import (
            ApiV1PricingOrganizationProductsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_provider_reference_error_component import (
            ApiV1PricingOrganizationProductsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_reconciliation_enabled_error_component import (
            ApiV1PricingOrganizationProductsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_sla_availability_error_component import (
            ApiV1PricingOrganizationProductsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_sla_target_error_component import (
            ApiV1PricingOrganizationProductsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_slo_availability_error_component import (
            ApiV1PricingOrganizationProductsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_slo_target_error_component import (
            ApiV1PricingOrganizationProductsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_target_availability_error_component import (
            ApiV1PricingOrganizationProductsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_tolerations_error_component import (
            ApiV1PricingOrganizationProductsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingOrganizationProductsUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateCatalogueAppErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateAutoManagedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateActiveFromErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateActiveUntilErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateAgreedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingOrganizationProductsUpdateAgreedPriceReasonErrorComponent):
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
        from ..models.api_v1_pricing_organization_products_update_active_from_error_component import (
            ApiV1PricingOrganizationProductsUpdateActiveFromErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_active_until_error_component import (
            ApiV1PricingOrganizationProductsUpdateActiveUntilErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_agreed_price_error_component import (
            ApiV1PricingOrganizationProductsUpdateAgreedPriceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_agreed_price_reason_error_component import (
            ApiV1PricingOrganizationProductsUpdateAgreedPriceReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_annotations_error_component import (
            ApiV1PricingOrganizationProductsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_archived_at_error_component import (
            ApiV1PricingOrganizationProductsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_archived_error_component import (
            ApiV1PricingOrganizationProductsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_archived_reason_error_component import (
            ApiV1PricingOrganizationProductsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_auto_managed_error_component import (
            ApiV1PricingOrganizationProductsUpdateAutoManagedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_catalogue_app_error_component import (
            ApiV1PricingOrganizationProductsUpdateCatalogueAppErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_content_type_error_component import (
            ApiV1PricingOrganizationProductsUpdateContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_criticality_error_component import (
            ApiV1PricingOrganizationProductsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_debug_mode_error_component import (
            ApiV1PricingOrganizationProductsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_display_name_error_component import (
            ApiV1PricingOrganizationProductsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_internal_note_error_component import (
            ApiV1PricingOrganizationProductsUpdateInternalNoteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_kind_error_component import (
            ApiV1PricingOrganizationProductsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_labels_error_component import (
            ApiV1PricingOrganizationProductsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_name_error_component import (
            ApiV1PricingOrganizationProductsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_non_field_errors_error_component import (
            ApiV1PricingOrganizationProductsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_object_id_error_component import (
            ApiV1PricingOrganizationProductsUpdateObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_platform_service_error_component import (
            ApiV1PricingOrganizationProductsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_provider_error_component import (
            ApiV1PricingOrganizationProductsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_provider_id_error_component import (
            ApiV1PricingOrganizationProductsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_provider_reference_error_component import (
            ApiV1PricingOrganizationProductsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_reconciliation_enabled_error_component import (
            ApiV1PricingOrganizationProductsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_sla_availability_error_component import (
            ApiV1PricingOrganizationProductsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_sla_target_error_component import (
            ApiV1PricingOrganizationProductsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_slo_availability_error_component import (
            ApiV1PricingOrganizationProductsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_slo_target_error_component import (
            ApiV1PricingOrganizationProductsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_target_availability_error_component import (
            ApiV1PricingOrganizationProductsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_organization_products_update_tolerations_error_component import (
            ApiV1PricingOrganizationProductsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingOrganizationProductsUpdateActiveFromErrorComponent
                | ApiV1PricingOrganizationProductsUpdateActiveUntilErrorComponent
                | ApiV1PricingOrganizationProductsUpdateAgreedPriceErrorComponent
                | ApiV1PricingOrganizationProductsUpdateAgreedPriceReasonErrorComponent
                | ApiV1PricingOrganizationProductsUpdateAnnotationsErrorComponent
                | ApiV1PricingOrganizationProductsUpdateArchivedAtErrorComponent
                | ApiV1PricingOrganizationProductsUpdateArchivedErrorComponent
                | ApiV1PricingOrganizationProductsUpdateArchivedReasonErrorComponent
                | ApiV1PricingOrganizationProductsUpdateAutoManagedErrorComponent
                | ApiV1PricingOrganizationProductsUpdateCatalogueAppErrorComponent
                | ApiV1PricingOrganizationProductsUpdateContentTypeErrorComponent
                | ApiV1PricingOrganizationProductsUpdateCriticalityErrorComponent
                | ApiV1PricingOrganizationProductsUpdateDebugModeErrorComponent
                | ApiV1PricingOrganizationProductsUpdateDisplayNameErrorComponent
                | ApiV1PricingOrganizationProductsUpdateInternalNoteErrorComponent
                | ApiV1PricingOrganizationProductsUpdateKindErrorComponent
                | ApiV1PricingOrganizationProductsUpdateLabelsErrorComponent
                | ApiV1PricingOrganizationProductsUpdateNameErrorComponent
                | ApiV1PricingOrganizationProductsUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingOrganizationProductsUpdateObjectIdErrorComponent
                | ApiV1PricingOrganizationProductsUpdatePlatformServiceErrorComponent
                | ApiV1PricingOrganizationProductsUpdateProviderErrorComponent
                | ApiV1PricingOrganizationProductsUpdateProviderIdErrorComponent
                | ApiV1PricingOrganizationProductsUpdateProviderReferenceErrorComponent
                | ApiV1PricingOrganizationProductsUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingOrganizationProductsUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsUpdateSlaTargetErrorComponent
                | ApiV1PricingOrganizationProductsUpdateSloAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsUpdateSloTargetErrorComponent
                | ApiV1PricingOrganizationProductsUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingOrganizationProductsUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_0 = (
                        ApiV1PricingOrganizationProductsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_1 = (
                        ApiV1PricingOrganizationProductsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_2 = (
                        ApiV1PricingOrganizationProductsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_3 = (
                        ApiV1PricingOrganizationProductsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_4 = (
                        ApiV1PricingOrganizationProductsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_5 = (
                        ApiV1PricingOrganizationProductsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_6 = (
                        ApiV1PricingOrganizationProductsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_7 = (
                        ApiV1PricingOrganizationProductsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_8 = (
                        ApiV1PricingOrganizationProductsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_9 = (
                        ApiV1PricingOrganizationProductsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_10 = (
                        ApiV1PricingOrganizationProductsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_11 = (
                        ApiV1PricingOrganizationProductsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_12 = (
                        ApiV1PricingOrganizationProductsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_13 = (
                        ApiV1PricingOrganizationProductsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_14 = (
                        ApiV1PricingOrganizationProductsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_15 = (
                        ApiV1PricingOrganizationProductsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_16 = (
                        ApiV1PricingOrganizationProductsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_17 = (
                        ApiV1PricingOrganizationProductsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_18 = (
                        ApiV1PricingOrganizationProductsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_19 = (
                        ApiV1PricingOrganizationProductsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_20 = (
                        ApiV1PricingOrganizationProductsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_21 = (
                        ApiV1PricingOrganizationProductsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_22 = (
                        ApiV1PricingOrganizationProductsUpdateCatalogueAppErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_23 = (
                        ApiV1PricingOrganizationProductsUpdateContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_24 = (
                        ApiV1PricingOrganizationProductsUpdateObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_25 = (
                        ApiV1PricingOrganizationProductsUpdateAutoManagedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_26 = (
                        ApiV1PricingOrganizationProductsUpdateActiveFromErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_27 = (
                        ApiV1PricingOrganizationProductsUpdateActiveUntilErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_28 = (
                        ApiV1PricingOrganizationProductsUpdateAgreedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_organization_products_update_error_type_29 = (
                        ApiV1PricingOrganizationProductsUpdateAgreedPriceReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_organization_products_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_organization_products_update_error_type_30 = (
                    ApiV1PricingOrganizationProductsUpdateInternalNoteErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_organization_products_update_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_organization_products_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_organization_products_update_validation_error.additional_properties = d
        return api_v1_pricing_organization_products_update_validation_error

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
