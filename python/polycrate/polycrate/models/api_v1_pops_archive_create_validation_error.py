from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pops_archive_create_annotations_error_component import (
        ApiV1PopsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_archived_at_error_component import (
        ApiV1PopsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_archived_error_component import (
        ApiV1PopsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_archived_reason_error_component import (
        ApiV1PopsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_city_error_component import ApiV1PopsArchiveCreateCityErrorComponent
    from ..models.api_v1_pops_archive_create_country_error_component import ApiV1PopsArchiveCreateCountryErrorComponent
    from ..models.api_v1_pops_archive_create_criticality_error_component import (
        ApiV1PopsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_debug_mode_error_component import (
        ApiV1PopsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_description_error_component import (
        ApiV1PopsArchiveCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_display_name_error_component import (
        ApiV1PopsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_kind_error_component import ApiV1PopsArchiveCreateKindErrorComponent
    from ..models.api_v1_pops_archive_create_labels_error_component import ApiV1PopsArchiveCreateLabelsErrorComponent
    from ..models.api_v1_pops_archive_create_latitude_error_component import (
        ApiV1PopsArchiveCreateLatitudeErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_longitude_error_component import (
        ApiV1PopsArchiveCreateLongitudeErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_name_error_component import ApiV1PopsArchiveCreateNameErrorComponent
    from ..models.api_v1_pops_archive_create_non_field_errors_error_component import (
        ApiV1PopsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_platform_service_error_component import (
        ApiV1PopsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_pop_endpoint_remote_address_error_component import (
        ApiV1PopsArchiveCreatePopEndpointRemoteAddressErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_provider_entity_id_error_component import (
        ApiV1PopsArchiveCreateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_provider_error_component import (
        ApiV1PopsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_provider_id_error_component import (
        ApiV1PopsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_provider_reference_error_component import (
        ApiV1PopsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_reconciliation_enabled_error_component import (
        ApiV1PopsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_region_error_component import ApiV1PopsArchiveCreateRegionErrorComponent
    from ..models.api_v1_pops_archive_create_sla_availability_error_component import (
        ApiV1PopsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_sla_target_error_component import (
        ApiV1PopsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_slo_availability_error_component import (
        ApiV1PopsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_slo_target_error_component import (
        ApiV1PopsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_target_availability_error_component import (
        ApiV1PopsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pops_archive_create_tolerations_error_component import (
        ApiV1PopsArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PopsArchiveCreateValidationError")


@_attrs_define
class ApiV1PopsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PopsArchiveCreateAnnotationsErrorComponent | ApiV1PopsArchiveCreateArchivedAtErrorComponent |
            ApiV1PopsArchiveCreateArchivedErrorComponent | ApiV1PopsArchiveCreateArchivedReasonErrorComponent |
            ApiV1PopsArchiveCreateCityErrorComponent | ApiV1PopsArchiveCreateCountryErrorComponent |
            ApiV1PopsArchiveCreateCriticalityErrorComponent | ApiV1PopsArchiveCreateDebugModeErrorComponent |
            ApiV1PopsArchiveCreateDescriptionErrorComponent | ApiV1PopsArchiveCreateDisplayNameErrorComponent |
            ApiV1PopsArchiveCreateKindErrorComponent | ApiV1PopsArchiveCreateLabelsErrorComponent |
            ApiV1PopsArchiveCreateLatitudeErrorComponent | ApiV1PopsArchiveCreateLongitudeErrorComponent |
            ApiV1PopsArchiveCreateNameErrorComponent | ApiV1PopsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1PopsArchiveCreatePlatformServiceErrorComponent |
            ApiV1PopsArchiveCreatePopEndpointRemoteAddressErrorComponent |
            ApiV1PopsArchiveCreateProviderEntityIdErrorComponent | ApiV1PopsArchiveCreateProviderErrorComponent |
            ApiV1PopsArchiveCreateProviderIdErrorComponent | ApiV1PopsArchiveCreateProviderReferenceErrorComponent |
            ApiV1PopsArchiveCreateReconciliationEnabledErrorComponent | ApiV1PopsArchiveCreateRegionErrorComponent |
            ApiV1PopsArchiveCreateSlaAvailabilityErrorComponent | ApiV1PopsArchiveCreateSlaTargetErrorComponent |
            ApiV1PopsArchiveCreateSloAvailabilityErrorComponent | ApiV1PopsArchiveCreateSloTargetErrorComponent |
            ApiV1PopsArchiveCreateTargetAvailabilityErrorComponent | ApiV1PopsArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PopsArchiveCreateAnnotationsErrorComponent
        | ApiV1PopsArchiveCreateArchivedAtErrorComponent
        | ApiV1PopsArchiveCreateArchivedErrorComponent
        | ApiV1PopsArchiveCreateArchivedReasonErrorComponent
        | ApiV1PopsArchiveCreateCityErrorComponent
        | ApiV1PopsArchiveCreateCountryErrorComponent
        | ApiV1PopsArchiveCreateCriticalityErrorComponent
        | ApiV1PopsArchiveCreateDebugModeErrorComponent
        | ApiV1PopsArchiveCreateDescriptionErrorComponent
        | ApiV1PopsArchiveCreateDisplayNameErrorComponent
        | ApiV1PopsArchiveCreateKindErrorComponent
        | ApiV1PopsArchiveCreateLabelsErrorComponent
        | ApiV1PopsArchiveCreateLatitudeErrorComponent
        | ApiV1PopsArchiveCreateLongitudeErrorComponent
        | ApiV1PopsArchiveCreateNameErrorComponent
        | ApiV1PopsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1PopsArchiveCreatePlatformServiceErrorComponent
        | ApiV1PopsArchiveCreatePopEndpointRemoteAddressErrorComponent
        | ApiV1PopsArchiveCreateProviderEntityIdErrorComponent
        | ApiV1PopsArchiveCreateProviderErrorComponent
        | ApiV1PopsArchiveCreateProviderIdErrorComponent
        | ApiV1PopsArchiveCreateProviderReferenceErrorComponent
        | ApiV1PopsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1PopsArchiveCreateRegionErrorComponent
        | ApiV1PopsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1PopsArchiveCreateSlaTargetErrorComponent
        | ApiV1PopsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1PopsArchiveCreateSloTargetErrorComponent
        | ApiV1PopsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1PopsArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pops_archive_create_annotations_error_component import (
            ApiV1PopsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_archived_at_error_component import (
            ApiV1PopsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_archived_error_component import (
            ApiV1PopsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_archived_reason_error_component import (
            ApiV1PopsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_city_error_component import (
            ApiV1PopsArchiveCreateCityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_country_error_component import (
            ApiV1PopsArchiveCreateCountryErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_criticality_error_component import (
            ApiV1PopsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_debug_mode_error_component import (
            ApiV1PopsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_description_error_component import (
            ApiV1PopsArchiveCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_display_name_error_component import (
            ApiV1PopsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_kind_error_component import (
            ApiV1PopsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_labels_error_component import (
            ApiV1PopsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_latitude_error_component import (
            ApiV1PopsArchiveCreateLatitudeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_longitude_error_component import (
            ApiV1PopsArchiveCreateLongitudeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_name_error_component import (
            ApiV1PopsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_non_field_errors_error_component import (
            ApiV1PopsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_platform_service_error_component import (
            ApiV1PopsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_provider_entity_id_error_component import (
            ApiV1PopsArchiveCreateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_provider_error_component import (
            ApiV1PopsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_provider_id_error_component import (
            ApiV1PopsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_provider_reference_error_component import (
            ApiV1PopsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_reconciliation_enabled_error_component import (
            ApiV1PopsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_region_error_component import (
            ApiV1PopsArchiveCreateRegionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_sla_availability_error_component import (
            ApiV1PopsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_sla_target_error_component import (
            ApiV1PopsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_slo_availability_error_component import (
            ApiV1PopsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_slo_target_error_component import (
            ApiV1PopsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_target_availability_error_component import (
            ApiV1PopsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_tolerations_error_component import (
            ApiV1PopsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PopsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateRegionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateCountryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateCityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateLatitudeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateLongitudeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PopsArchiveCreateProviderEntityIdErrorComponent):
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
        from ..models.api_v1_pops_archive_create_annotations_error_component import (
            ApiV1PopsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_archived_at_error_component import (
            ApiV1PopsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_archived_error_component import (
            ApiV1PopsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_archived_reason_error_component import (
            ApiV1PopsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_city_error_component import (
            ApiV1PopsArchiveCreateCityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_country_error_component import (
            ApiV1PopsArchiveCreateCountryErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_criticality_error_component import (
            ApiV1PopsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_debug_mode_error_component import (
            ApiV1PopsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_description_error_component import (
            ApiV1PopsArchiveCreateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_display_name_error_component import (
            ApiV1PopsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_kind_error_component import (
            ApiV1PopsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_labels_error_component import (
            ApiV1PopsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_latitude_error_component import (
            ApiV1PopsArchiveCreateLatitudeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_longitude_error_component import (
            ApiV1PopsArchiveCreateLongitudeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_name_error_component import (
            ApiV1PopsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_non_field_errors_error_component import (
            ApiV1PopsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_platform_service_error_component import (
            ApiV1PopsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_pop_endpoint_remote_address_error_component import (
            ApiV1PopsArchiveCreatePopEndpointRemoteAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_provider_entity_id_error_component import (
            ApiV1PopsArchiveCreateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_provider_error_component import (
            ApiV1PopsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_provider_id_error_component import (
            ApiV1PopsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_provider_reference_error_component import (
            ApiV1PopsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_reconciliation_enabled_error_component import (
            ApiV1PopsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_region_error_component import (
            ApiV1PopsArchiveCreateRegionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_sla_availability_error_component import (
            ApiV1PopsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_sla_target_error_component import (
            ApiV1PopsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_slo_availability_error_component import (
            ApiV1PopsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_slo_target_error_component import (
            ApiV1PopsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_target_availability_error_component import (
            ApiV1PopsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pops_archive_create_tolerations_error_component import (
            ApiV1PopsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PopsArchiveCreateAnnotationsErrorComponent
                | ApiV1PopsArchiveCreateArchivedAtErrorComponent
                | ApiV1PopsArchiveCreateArchivedErrorComponent
                | ApiV1PopsArchiveCreateArchivedReasonErrorComponent
                | ApiV1PopsArchiveCreateCityErrorComponent
                | ApiV1PopsArchiveCreateCountryErrorComponent
                | ApiV1PopsArchiveCreateCriticalityErrorComponent
                | ApiV1PopsArchiveCreateDebugModeErrorComponent
                | ApiV1PopsArchiveCreateDescriptionErrorComponent
                | ApiV1PopsArchiveCreateDisplayNameErrorComponent
                | ApiV1PopsArchiveCreateKindErrorComponent
                | ApiV1PopsArchiveCreateLabelsErrorComponent
                | ApiV1PopsArchiveCreateLatitudeErrorComponent
                | ApiV1PopsArchiveCreateLongitudeErrorComponent
                | ApiV1PopsArchiveCreateNameErrorComponent
                | ApiV1PopsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1PopsArchiveCreatePlatformServiceErrorComponent
                | ApiV1PopsArchiveCreatePopEndpointRemoteAddressErrorComponent
                | ApiV1PopsArchiveCreateProviderEntityIdErrorComponent
                | ApiV1PopsArchiveCreateProviderErrorComponent
                | ApiV1PopsArchiveCreateProviderIdErrorComponent
                | ApiV1PopsArchiveCreateProviderReferenceErrorComponent
                | ApiV1PopsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1PopsArchiveCreateRegionErrorComponent
                | ApiV1PopsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1PopsArchiveCreateSlaTargetErrorComponent
                | ApiV1PopsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1PopsArchiveCreateSloTargetErrorComponent
                | ApiV1PopsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1PopsArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_0 = (
                        ApiV1PopsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_1 = (
                        ApiV1PopsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_2 = (
                        ApiV1PopsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_3 = (
                        ApiV1PopsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_4 = (
                        ApiV1PopsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_5 = (
                        ApiV1PopsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_6 = (
                        ApiV1PopsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_7 = (
                        ApiV1PopsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_8 = (
                        ApiV1PopsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_9 = (
                        ApiV1PopsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_10 = (
                        ApiV1PopsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_11 = (
                        ApiV1PopsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_12 = (
                        ApiV1PopsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_13 = (
                        ApiV1PopsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_14 = (
                        ApiV1PopsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_15 = (
                        ApiV1PopsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_16 = (
                        ApiV1PopsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_17 = (
                        ApiV1PopsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_18 = (
                        ApiV1PopsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_19 = (
                        ApiV1PopsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_20 = (
                        ApiV1PopsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_21 = (
                        ApiV1PopsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_22 = (
                        ApiV1PopsArchiveCreateRegionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_23 = (
                        ApiV1PopsArchiveCreateCountryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_24 = (
                        ApiV1PopsArchiveCreateCityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_25 = (
                        ApiV1PopsArchiveCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_26 = (
                        ApiV1PopsArchiveCreateLatitudeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_27 = (
                        ApiV1PopsArchiveCreateLongitudeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pops_archive_create_error_type_28 = (
                        ApiV1PopsArchiveCreateProviderEntityIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pops_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pops_archive_create_error_type_29 = (
                    ApiV1PopsArchiveCreatePopEndpointRemoteAddressErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pops_archive_create_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pops_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pops_archive_create_validation_error.additional_properties = d
        return api_v1_pops_archive_create_validation_error

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
